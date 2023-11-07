import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pydantic import BaseModel

class User(BaseModel):
    username: str
    email: str
    _password: str