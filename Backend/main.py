from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer



from routes.Automate import AutomateRoute
from routes.Charts.valueCounts import valueCountsRoute    
from routes.Charts.Sales import SalesRoute 
from routes.Forecast import ForecastRoute
from routes.Charts.Top20s import Top20sRoute
from routes.Charts.Negative import NegativeRoute
from auth.LoggingRegistration import LoginRegistrationRoute
from routes.AllDataRetrive import AllDataRetriveRoute
app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app.include_router(AutomateRoute,
    prefix="/Automate",
    tags=["Automate"],)

app.include_router(valueCountsRoute, prefix="/ValueCounts", tags=["Froute - ValueCounts"])
app.include_router(SalesRoute, prefix="/Sales", tags=["Froute - Sales"])
app.include_router(ForecastRoute, prefix="/Forecast", tags=["Froute - Forecast"])
app.include_router(Top20sRoute, prefix="/Top20s", tags=["Froute - Top20s"])
app.include_router(NegativeRoute, prefix="/Negative", tags=["Froute - Negative"])
app.include_router(LoginRegistrationRoute, tags=["LoginRegistration"])
app.include_router(AllDataRetriveRoute,tags=['View_all_Data'])


# React app is running on port 3000
app.add_middleware(
    CORSMiddleware,
    allow_origins=[("http://localhost:3000")],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)
# Vite app is running on port 5173
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)
