from rich.console import Console
from rich.markdown import Markdown

console = Console()
md = Markdown("""
# Qoruz App  
Welcome to **Qoruz** – the creator intelligence platform.  

- Find top influencers  
- Track engagement  
- Build campaigns faster  
""")

console.print(md)