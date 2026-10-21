#include <algorithm>
#include <cstdlib>
#include <utility>
#include <vector>
#include <fstream>
#include <iostream>
#include <string>
#include <chrono>
#include <stdexcept>
// Native signed128 arithmetic handles propagation; GMP is used only for exact domain squares.
// The pinned operator header128 describes the prior reference grid; this backend uses104.
// Minimal declarations of the installed GNU GMP Linux64 ABI. No internal limbs are accessed.
// This backend is platform-bound; source replay must retain the ABI/probe receipt.
extern "C" {
struct mpzabi {int alloc,size;unsigned long*limbs;};
void __gmpz_init(mpzabi*);void __gmpz_clear(mpzabi*);void __gmpz_set(mpzabi*,const mpzabi*);
void __gmpz_set_si(mpzabi*,long);int __gmpz_set_str(mpzabi*,const char*,int);
char* __gmpz_get_str(char*,int,const mpzabi*);size_t __gmpz_sizeinbase(const mpzabi*,int);
void __gmpz_add(mpzabi*,const mpzabi*,const mpzabi*);void __gmpz_addmul(mpzabi*,const mpzabi*,const mpzabi*);
void __gmpz_addmul_ui(mpzabi*,const mpzabi*,unsigned long);void __gmpz_submul_ui(mpzabi*,const mpzabi*,unsigned long);
void __gmpz_mul_2exp(mpzabi*,const mpzabi*,unsigned long);void __gmpz_tdiv_q_2exp(mpzabi*,const mpzabi*,unsigned long);
unsigned long __gmpz_tdiv_q_ui(mpzabi*,const mpzabi*,unsigned long);
void __gmpz_neg(mpzabi*,const mpzabi*);int __gmpz_cmp(const mpzabi*,const mpzabi*);
extern const char*__gmp_version;
}
struct I {
 mpzabi z;I(){__gmpz_init(&z);}I(long v):I(){__gmpz_set_si(&z,v);}I(const I&v):I(){__gmpz_set(&z,&v.z);}I(I&&v)noexcept:I(){std::swap(z,v.z);}~I(){__gmpz_clear(&z);}I&operator=(const I&v){__gmpz_set(&z,&v.z);return *this;}I&operator=(I&&v)noexcept{std::swap(z,v.z);return *this;}
 I&operator+=(const I&v){__gmpz_add(&z,&z,&v.z);return *this;}
};
I shifted(const I&x,int b){I y;__gmpz_mul_2exp(&y.z,&x.z,b);return y;}
std::istream&operator>>(std::istream&f,I&x){std::string s;if(f>>s){if(s.empty()||s.find_first_not_of("-0123456789")!=std::string::npos||__gmpz_set_str(&x.z,s.c_str(),10))f.setstate(std::ios::failbit);}return f;}
std::ostream&operator<<(std::ostream&f,const I&x){std::vector<char>b(__gmpz_sizeinbase(&x.z,10)+3);__gmpz_get_str(b.data(),10,&x.z);return f<<b.data();}
using N=__int128_t;using U=__uint128_t;using V=std::vector<N>;
std::string decimal(N x){bool neg=x<0;U u=neg?U(-(x+1))+1:U(x);std::string s;do{s.push_back(char('0'+u%10));u/=10;}while(u);if(neg)s.push_back('-');std::reverse(s.begin(),s.end());return s;}
N readnative(const std::string&s){bool neg=!s.empty()&&s[0]=='-';size_t i=neg?1:0;if(i==s.size())throw std::runtime_error("bad integer");U u=0,cap=U(1)<<112;for(;i<s.size();i++){if(s[i]<'0'||s[i]>'9')throw std::runtime_error("bad integer");unsigned d=s[i]-'0';if(u>(cap-d)/10)throw std::runtime_error("input scalar out of range");u=10*u+d;}return neg?-N(u):N(u);}
N up(N x,int bits){return x*(N(1)<<bits);}N down(N x,int bits){return x/(N(1)<<bits);}
void termdomain(N x){const N cap=N(1)<<119;if(x<=-cap||x>=cap)throw std::runtime_error("native term bound exceeded");}
struct Edge{int j,w;};
struct Action{
 int n,c,m,L,b;std::vector<int>obs;std::vector<std::vector<Edge>>rows;
 Action(const std::string&path){std::ifstream f(path);if(!(f>>n>>c>>m>>L>>b)||n!=2640||c!=62||m!=4096||L!=40||b!=128)throw std::runtime_error("bad frozen dimensions");obs.resize(c);for(int&i:obs){f>>i;if(i<0||i>=n)throw std::runtime_error("bad observer");}rows.resize(n);int ne=0;if(!(f>>ne)||ne!=14880)throw std::runtime_error("bad incidence count");for(int t=0;t<ne;t++){int i,j,w;f>>i>>j>>w;if(!f||i<0||i>=n||j<0||j>=n||(w!=2&&w!=-2&&w!=3&&w!=-3))throw std::runtime_error("bad incidence");rows[i].push_back({j,w});}std::string trailing;if(f>>trailing)throw std::runtime_error("trailing operator data");for(auto&r:rows){int s=0;for(auto e:r)s+=abs(e.w);if(s>24)throw std::runtime_error("row sum exceeds source bound");}}
 void domain(const V&v,int bits,int radius){I sum,cap(radius),cap2,t;for(N x:v){std::string s=decimal(x);if(__gmpz_set_str(&t.z,s.c_str(),10))throw std::runtime_error("GMP scalar conversion");__gmpz_addmul(&sum.z,&t.z,&t.z);}cap=shifted(cap,bits);__gmpz_addmul(&cap2.z,&cap.z,&cap.z);if(__gmpz_cmp(&sum.z,&cap2.z)>0)throw std::runtime_error("input exceeds certified domain");}
 template<int k>void termstep(V&term,V&out,V&next,int sign){
  for(N v:term)termdomain(v);
  for(int i=0;i<n;i++){N z=0,extra=0;for(auto e:rows[i]){N v=term[e.j];if(sign*e.w>0){z+=v;if(abs(e.w)==3)extra+=v;}else{z-=v;if(abs(e.w)==3)extra-=v;}}next[i]=(z+z+extra)/(4*k);termdomain(next[i]);out[i]+=next[i];}
  term.swap(next);
  if constexpr(k<40)termstep<k+1>(term,out,next,sign);
 }
 V step(const V&x,int sign){V term=x,out=x,next(n);termstep<1>(term,out,next,sign);return out;}
 V forward(const V&x){domain(x,96,2048);V state(n),out(c*m);for(int i=0;i<n;i++)state[i]=up(x[i],8);for(int j=0;j<m;j++){for(int k=0;k<c;k++)out[j*c+k]=::down(state[obs[k]],14);if(j+1<m)state=step(state,1);if(j%512==0)std::cerr<<"forward "<<j<<"/4096\n";}return out;}
 V adjoint(const V&y){domain(y,96,2049);V state(n);for(int j=m-1;j>=0;j--){for(int k=0;k<c;k++)state[obs[k]]+=up(y[j*c+k],2);if(j>0)state=step(state,-1);if(j%512==0)std::cerr<<"adjoint "<<j<<"/4096\n";}V out(n);for(int i=0;i<n;i++)out[i]=::down(state[i],8);return out;}
};
int main(int argc,char**argv){try{if(argc!=5)throw std::runtime_error("usage: action OPERATOR forward|adjoint INPUT OUTPUT");Action a(argv[1]);std::string mode=argv[2];std::cerr<<"Native104/GMPdomain "<<__gmp_version<<" longbits="<<8*sizeof(unsigned long)<<"\n";if(sizeof(unsigned long)!=8||sizeof(mpzabi)!=16)throw std::runtime_error("unsupported GMP ABI");if(mode!="forward"&&mode!="adjoint"&&mode!="step+"&&mode!="step-")throw std::runtime_error("unknown mode");int count=mode=="adjoint"?a.m*a.c:a.n;std::ifstream f(argv[3]);V v(count);for(N&x:v){std::string text;if(!(f>>text))throw std::runtime_error("invalid input length/value");x=readnative(text);}std::string extra;if(f>>extra)throw std::runtime_error("extra input");auto t=std::chrono::steady_clock::now();V out;if(mode=="forward")out=a.forward(v);else if(mode=="adjoint")out=a.adjoint(v);else{a.domain(v,96,2048);for(N&x:v)x=up(x,8);out=a.step(v,mode=="step+"?1:-1);for(N&x:out)x=down(x,8);}std::ofstream g(argv[4]);if(!g)throw std::runtime_error("cannot create output");for(N x:out)g<<decimal(x)<<'\n';g.close();if(!g)throw std::runtime_error("output write failed");std::cout<<"PASS "<<mode<<" input="<<v.size()<<" output="<<out.size()<<" seconds="<<std::chrono::duration<double>(std::chrono::steady_clock::now()-t).count()<<"\n";return 0;}catch(const std::exception&e){std::cerr<<"REJECT "<<e.what()<<'\n';return 1;}}
