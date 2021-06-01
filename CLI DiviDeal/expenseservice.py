from user import*
from split import*
from expense import*
from expensetype import*
from math import*

class Expenseservice:
    def createexpense(extype,amount,paidby,splits):
        if(extype==Expensetype[0]):
            return exactexpense(amount,paidby,splits)
        
        elif(extype==Expensetype[1]):
            for split in splits:
                split.__class__=percentsplit
                split.setAmount((amount*split.getpercent())/100.0)
            return percentexpense(amount,paidby,splits)
        
        elif(extype==Expensetype[2]):
            totalsplits=len(splits)
            splitAmount = (float(round(amount*100/totalsplits))/100.0)
            for split in splits:
                split.setAmount(splitAmount)
            splits[0].setAmount(splitAmount + (amount - splitAmount*totalsplits))
            return percentexpense(amount,paidby,splits)
        
        elif(extype==Expensetype[3]):
            totalshares = 0.0
            totalshareamt = 0.0
            for split in splits:
                split.__class__ = sharesplit
                totalshares += split.getshare()
            for split in splits:
                split.__class__ = sharesplit
                sharevalue = float(round((amount * split.getshare()) / totalshares, 2))
                totalshareamt += sharevalue
                split.setAmount(sharevalue)
            splits[0].setAmount(round(splits[0].getAmount() - (totalshareamt - amount), 2))
            return SharesExpense(amount, paidby, splits)

        elif(extype == Expensetype[4]):
            for split in splits:
                split.__class__ = adjustsplit
                amount -= split.getadjust()

            totalsplits = len(splits)
            splitamount = float(round(amount * 100 / totalsplits, 2)) / 100.0
            for split in splits:
                split.setAmount(round(split.getadjust() + splitamount, 2))
            splits[0].setAmount(round(splits[0].getadjust() + splitamount + (amount - splitamount * totalsplits), 2))
            return AdjustExpense(amount, paidby, splits)
        else:
            return None
            
