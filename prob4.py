constraints = {
    "Aa": {"Rda": (2, 1), "Rsa": (2, 1), "Ap": (2, 2), "I": (1, 1)},
    "Ap": {"Rdp": (2, 1), "Rsp": (2, 1), "Aa": (2, 2), "I": (1, 1)},
    "Rda": {"Aa":(2,0),"I": (1, 1)},
    "Rsa": {"Aa":(2,0),"I": (1, 1)},
    "Rdp": {"Ap":(2,0),"I": (1, 1)},
    "Rsp": {"Ap":(2,0), "I": (1, 1)},
    "I": {"Aa": (1, 0), "Ap": (1, 0), "Rda": (1, 0), "Rsa": (1, 0), "Rdp": (1, 0), "Rsp": (1, 0)}
        
}
variables = {
    "Aa": range(1, 7),
    "Ap": range(1, 7),
    "Rda": range(1, 7),
    "Rsa": range(1, 7),
    "Rdp": range(1, 7),
    "Rsp": range(1, 7),
    "I": range(1, 7),
}
