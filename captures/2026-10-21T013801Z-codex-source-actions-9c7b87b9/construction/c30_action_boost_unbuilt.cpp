#include <boost/multiprecision/cpp_int.hpp>
#include <vector>
#include <fstream>
#include <iostream>
#include <string>
#include <chrono>
#include <stdexcept>
using namespace boost::multiprecision;
using I=number<cpp_int_backend<256,256,signed_magnitude,checked,void>>;
using V=std::vector<I>;
struct Edge{int j,w;};
struct Action{
 int n,c,m,L,b;std::vector<int>obs;std::vector<std::vector<Edge>>rows;
 Action(const std::string&path){std::ifstream f(path);if(!(f>>n>>c>>m>>L>>b)||n!=2640||c!=62||m!=4096||L!=40||b!=128)throw std::runtime_error("bad frozen dimensions");obs.resize(c);for(int&i:obs){f>>i;if(i<0||i>=n)throw std::runtime_error("bad observer");}rows.resize(n);int ne;f>>ne;if(ne!=14880)throw std::runtime_error("bad incidence count");for(int t=0;t<ne;t++){int i,j,w;f>>i>>j>>w;if(!f||i<0||i>=n||j<0||j>=n||(w!=2&&w!=-2&&w!=3&&w!=-3))throw std::runtime_error("bad incidence");rows[i].push_back({j,w});}std::string trailing;if(f>>trailing)throw std::runtime_error("trailing operator data");for(auto&r:rows){int s=0;for(auto e:r)s+=abs(e.w);if(s>24)throw std::runtime_error("row sum exceeds source bound");}}
 void domain(const V&v,int bits,int radius){cpp_int s=0;for(const I&x:v){cpp_int t(x);s+=t*t;}cpp_int cap=cpp_int(radius)<<bits;if(s>cap*cap)throw std::runtime_error("input exceeds certified domain");}
 V step(const V&x,int sign){V term=x,out=x,next(n);for(int k=1;k<=L;k++){for(int i=0;i<n;i++){I z=0;for(auto e:rows[i])z+=term[e.j]*e.w;next[i]=(sign*z)/(4*k);out[i]+=next[i];}term.swap(next);}return out;}
 // Division of signed integers truncates toward zero. Its absolute error is<1 grid unit.
 I down(const I&x,int shift){return x/(I(1)<<shift);}
 V forward(const V&x){domain(x,96,2048);V state(n),out(c*m);for(int i=0;i<n;i++)state[i]=x[i]*(I(1)<<32);for(int j=0;j<m;j++){for(int k=0;k<c;k++)out[j*c+k]=down(state[obs[k]],38);if(j+1<m)state=step(state,1);if(j%512==0)std::cerr<<"forward "<<j<<"/4096\n";}return out;}
 V adjoint(const V&y){domain(y,96,2049);V state(n);for(int j=m-1;j>=0;j--){for(int k=0;k<c;k++)state[obs[k]]+=y[j*c+k]*(I(1)<<26);if(j>0)state=step(state,-1);if(j%512==0)std::cerr<<"adjoint "<<j<<"/4096\n";}V out(n);for(int i=0;i<n;i++)out[i]=down(state[i],32);return out;}
};
int main(int argc,char**argv){try{if(argc!=5)throw std::runtime_error("usage: action OPERATOR forward|adjoint INPUT OUTPUT");Action a(argv[1]);std::string mode=argv[2];if(mode!="forward"&&mode!="adjoint"&&mode!="step+"&&mode!="step-")throw std::runtime_error("unknown mode");int count=mode=="adjoint"?a.m*a.c:a.n;std::ifstream f(argv[3]);V v(count);for(I&x:v)if(!(f>>x))throw std::runtime_error("invalid input length/value");std::string extra;if(f>>extra)throw std::runtime_error("extra input");auto t=std::chrono::steady_clock::now();V out;if(mode=="forward")out=a.forward(v);else if(mode=="adjoint")out=a.adjoint(v);else{a.domain(v,96,2048);for(I&x:v)x*=I(1)<<32;out=a.step(v,mode=="step+"?1:-1);for(I&x:out)x=a.down(x,32);}std::ofstream g(argv[4]);if(!g)throw std::runtime_error("cannot create output");for(const I&x:out)g<<x<<'\n';g.close();if(!g)throw std::runtime_error("output write failed");std::cout<<"PASS "<<mode<<" input="<<v.size()<<" output="<<out.size()<<" seconds="<<std::chrono::duration<double>(std::chrono::steady_clock::now()-t).count()<<"\n";return 0;}catch(const std::exception&e){std::cerr<<"REJECT "<<e.what()<<'\n';return 1;}}
