import sys
sys.dont_write_bytecode=True
from pathlib import Path
import state,flux
p=Path(__file__).resolve().parent
state.main(p,False)
flux.main(p,False)
