# Making an application

To make your first app using Photon Start by importing it in you Project.py file.

`from Photon import *`

Now start by defining a class inheriting from `PhotonApplication`

```Python
class YourApp(PhotonApplication):
    def OnStart(self) -> None: ...
    def OnUpdate(self, dt: float) -> None: ...
    def OnEnd(self) -> None: ...
```

> Note that your subclass shoud overwrite the OnStart, OnUpdate and OnEnd methods.
> Also note that the dt will be in seconds.

Now you need to call the Main() method.

```python
if __name__ == '__main__':
    Main()
```

Here's a simple example:

```python
from Photon import *

class YourApp(PhotonApplication):
    def OnStart(self) -> None: pass
    
    def OnUpdate(self, dt: float) -> None:
        print("Hello, World")
        self.Close()
        
    def OnEnd(self) -> None: pass

if __name__ == "__main__":
    Main()
```
