# getting inputs--------------------------

weightOfJuwelery=float(input("Please enter you Need weight of gold:"))
ValueOfPoun=float(input("Please Enter now value of one poun:"))




# Cheack quantity of poun------------------

QuentityOfPoun=(weightOfJuwelery / 8)
print("Quntity of poun you have is:",QuentityOfPoun)




# worker cost for one poun-----------------

WorkerCostPoun =  ValueOfPoun * (25/100)
print("worker cost for one poun:",WorkerCostPoun)




# value in gold----------------------------

ValueOfGold = (QuentityOfPoun  *  ValueOfPoun)
print("Value in your gold:",ValueOfGold)





# Worker Cost---------------------------------

WorkerCost= (QuentityOfPoun *  QuentityOfPoun)
print("Worker cost is:",WorkerCost)






# Total cost for the juweleary-----------------------

TotalCost=  (WorkerCost + ValueOfGold )
print("Total cost for your juweleray:",TotalCost)


















                   
