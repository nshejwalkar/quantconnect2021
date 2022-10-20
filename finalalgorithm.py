#region imports
from AlgorithmImports import *
#endregion
import math
from numpy import log

class AlertOrangeSnake(QCAlgorithm):
    
    def Initialize(self):
        self.SetStartDate(2019, 1, 1)
        self.SetEndDate(2020, 7, 1)# Set Start Date
        self.SetCash(5000000)  # Set Strategy Cash
       
        #Energy
        self.AddEquity("CVX", Resolution.Hour)
        self.AddEquity("XOM", Resolution.Hour)
        #Retail
        self.AddEquity("LULU", Resolution.Hour)
        self.AddEquity("M", Resolution.Hour)
        self.AddEquity("JWN", Resolution.Hour)
        self.AddEquity("CMG", Resolution.Hour)
        self.AddEquity("TSN", Resolution.Hour)
        self.AddEquity("LL", Resolution.Hour)
        #Retech
        self.AddEquity("AMZN", Resolution.Hour)
        #Consumer Discretionary
        self.AddEquity("ECL", Resolution.Hour)
        self.AddEquity("NKE", Resolution.Hour)
        self.AddEquity("SBUX", Resolution.Hour)
        self.AddEquity("F", Resolution.Hour)
        self.AddEquity("GM", Resolution.Hour)
        self.AddEquity("TSN", Resolution.Hour)
        #Materials/Aerospace
        self.AddEquity("LMT", Resolution.Hour)
        self.AddEquity("BA", Resolution.Hour)
        self.AddEquity("AAL", Resolution.Hour)
        #Consumer Staples
        self.AddEquity("WMT", Resolution.Hour)
        self.AddEquity("COST", Resolution.Hour)
        #Healthcare
        self.AddEquity("MDT", Resolution.Hour)
        self.AddEquity("DHR", Resolution.Hour)
        self.AddEquity("AZN", Resolution.Hour)
        self.AddEquity("PFE", Resolution.Hour)
        self.AddEquity("LLY", Resolution.Hour)
        #Financials
        self.AddEquity("GS", Resolution.Hour)
        self.AddEquity("WFC", Resolution.Hour)
        #Information Technology
        self.AddEquity("AMD", Resolution.Hour)
        self.AddEquity("NVDA", Resolution.Hour)
        #Communication Services
        self.AddEquity("GOOG", Resolution.Hour)
        self.AddEquity("SE", Resolution.Hour)

        #Random
        self.AddEquity("JNUG", Resolution.Hour)
        self.AddEquity("ACB", Resolution.Hour)

        #"Precious Metals"
        self.AddEquity("GLD", Resolution.Hour)

    
        self.SetBenchmark("SPY")
    
        self.Stocks =  [ "CVX" , "XOM" , "F" , "GM", "M" , "JWN" , "CMG" , "LL" , "WMT" , "COST" , "TSN", "AMZN" , "LULU" , "ECL" , "AAL" , "BA" , "AZN" , "LLY", "PFE" , "DHR" , "MDT" , "GOOG" , "AMD" , "NVDA" , "GS" , "WFC", "GLD" , "JNUG" , "ACB"]
     #   
        
      

    def OnData(self, data):

        def atrgiv(df, n):
            sum1 = 0
            i = 1
            w = df.shape[0]
            while (i <= n):
                mm = df["high"].iloc[w - i] - df["low"].iloc[w - i]
                ax = abs(df["high"].iloc[w - i] - df["close"].iloc[w - i])
                an = abs(df["low"].iloc[w - i] - df["close"].iloc[w - i])
                li = [mm, ax, an]
                sum1 = sum1 + max(li)
                i = i + 1
                
            return sum1/n
            

        for Stock in self.Stocks:

            df = self.History(self.Symbol(Stock), 10, Resolution.Hour)
           

            HighS = df["high"].tail(4)
            LowS = df["low"].tail(4)
            self.Log(df)
            LowMin = LowS.min()
            HighMax = HighS.max()
            self.Log(HighMax)
            atr = atrgiv(df, 4)
            self.Log(atr)
            h1 = (log(HighMax - LowMin) - (log(atr)))/(log(4))
            self.Log(h1)

            HighS = df["high"].tail(5)
            LowS = df["low"].tail(5)
            LowMin = LowS.min()
            HighMax = HighS.max()
            atr = atrgiv(df, 5)
            h2 = (log(HighMax - LowMin) - (log(atr)))/(log(5))
            
            if (h2 > 0.5):
                h2 = h2 + 0.04
            elif(h2 < 0.5):
                h2 = h2 - 0.04
            else:
                h2 = h2 + 0
                
            HighS = df["high"].tail(6)
            LowS = df["low"].tail(6)
            LowMin = LowS.min()
            HighMax = HighS.max()
            atr = atrgiv(df, 6)
            h3 = (log(HighMax - LowMin) - (log(atr)))/(log(6))
            
            if (h3 > 0.5):
                h3 = h3 + 0.07
            elif(h2 < 0.5):
                h3 = h3 - 0.07
            else:
                h3 = h3 + 0

            HighS = df["high"].tail(7)
            LowS = df["low"].tail(7)
            LowMin = LowS.min()
            HighMax = HighS.max()
            atr = atrgiv(df, 7)
            h4 = (log(HighMax - LowMin) - (log(atr)))/(log(7))
            
            if (h4 > 0.5):
                h4 = h4 + 0.105
            elif(h2 < 0.5):
                h4 = h4 - 0.105
            else:
                h4 = h4 + 0

            HighS = df["high"].tail(8)
            LowS = df["low"].tail(8)
            LowMin = LowS.min()
            HighMax = HighS.max()
            atr = atrgiv(df, 8)
            h5 = (log(HighMax - LowMin) - (log(atr)))/(log(8))
            
            if (h5 > 0.5):
                h5 = h5 + 0.13
            elif(h2 < 0.5):
                h5 = h5 - 0.13
            else:
                h5 = h5 + 0

            HighS = df["high"].tail(9)
            LowS = df["low"].tail(9)
            LowMin = LowS.min()
            HighMax = HighS.max()
            atr = atrgiv(df, 9)
            h6 = (log(HighMax - LowMin) - (log(atr)))/(log(9))
            
            if (h6 > 0.5):
                h6 = h6 + 0.15
            elif(h2 < 0.5):
                h6 = h6 - 0.15
            else:
                h6 = h6 + 0

            hlist = [h1, h2, h3, h4, h5, h6]
            havg = (h1 + h2 + h3 + h4 + h5 + h6)/6
            PriceNow = df["close"][-1]
            PriceThen = df["close"][-3]
            Price3 = df["close"][-3]
            Price4 = df["close"][-4]
            Price5 = df["close"][-5]
            
            sma = (PriceNow + PriceThen + Price3 + Price4 + Price5)/5
            
            if ((min(hlist) > 0.5) & (PriceNow > PriceThen) & (df["close"][-1] > sma) & (max(hlist) > 0.6)):
                self.SetHoldings(Stock, 0.1)
                
            if ((min(hlist) > 0.7) & (PriceNow < PriceThen) & (df["close"][-1] < sma) & (max(hlist) > 0.82)):
                self.SetHoldings(Stock, -0.1)

            if (max(hlist) <= 0.4):
                self.Liquidate(Stock)
             
        

            #if ((max(hlist) <= 0.51)):
                #self.SetHoldings(Stock, 0.20)
# If H(N) > .5 then H +[2 = 0] [3 = .08] [4 = .13] [5 = .17] [6 = .195] [7 = .22] [8 = .24] [9 = .255] [10 = .27] [11 = .2825] [ 12 = .2925] [ 13 = .3]
# else if H(N) < .5 then H - [2 = 0] [3 = .08] [4 = .13] [5 = .17] [6 = .195] [7 = .22] [8 = .24] [9 = .255] [10 = .27] [11 = .2825] [ 12 = .2925] [ 13 = .3] else 0
        # Create a set of 10 hurst values, lengths n = 2, 4, 5, 6, 8, 10.
        # Signal Strength = 
        # def atr = MovingAverage(averageType, TrueRange(high, close, low), N);
        # def Hurst's exponent = (Log(hh - ll) - Log(atr)) / (Log(N));