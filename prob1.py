constraints = {
    "Aa": {"Rda": (10, 1), "Rsa": (10, 1), "Ap": (10, 2), "I": (3, 1)},
    "Ap": {"Rdp": (10, 1), "Rsp": (10, 1), "Aa": (10, 2), "I": (3, 1)},
    "Rda": {"Aa":(10,0),"Dda": (1, 1), "I": (3, 1)},
    "Rsa": {"Aa":(10,0),"Dsa": (1, 1), "I": (3, 1)},
    "Rdp": {"Ap":(10,0),"Ddp": (1, 1), "I": (3, 1)},
    "Rsp": {"Ap":(10,0),"Dsp": (1, 1), "I": (3, 1)},
    "Dda": {"Rda":(1,0),"Cda": (2, 1), "I": (3, 1)},
    "Dsa": {"Rsa":(1,0),"Csa": (2, 1), "I": (3, 1)},
    "Ddp": {"Rdp":(1,0),"Cdp": (2, 1), "I": (3, 1)},
    "Dsp": {"Rsp":(1,0),"Csp": (2, 1), "I": (3, 1)},
    "Cda": {"Dda":(2,0),"I": (3, 1)},
    "Csa": {"Dsa":(2,0),"I": (3, 1)},
    "Cdp": {"Ddp":(2,0),"I": (3, 1)},
    "Csp": {"Dsp":(2,0),"I": (3, 1)},
    "I": {"Aa": (3, 0), "Ap": (3, 0), "Rda": (3, 0), "Rsa": (3, 0), "Rdp": (3, 0), "Rsp": (3, 0), "Dda": (3, 0), "Dsa": (3, 0), "Ddp": (3, 0), 
          "Dsp": (3, 0), "Cda": (3, 0), "Csa": (3, 0), "Cdp": (3, 0), "Csp": (3, 0)}
        
}
variables = {
    "Aa": range(1, 31),
    "Ap": range(1, 31),
    "Rda": range(1, 31),
    "Rsa": range(1, 31),
    "Rdp": range(1, 31),
    "Rsp": range(1, 31),
    "Dda": range(1, 31),
    "Dsa": range(1, 31),
    "Ddp": range(1, 31),
    "Dsp": range(1, 31),
    "Cda": range(1, 31),
    "Csa": range(1, 31),
    "Cdp": range(1, 31),
    "Csp": range(1, 31),
    "I": range(1, 31),
}
