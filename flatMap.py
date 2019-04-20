from pyspark import SparkConf,SparkContext
conf = SparkConf().setAppName("Theorem LLC")
sc = SparkContext(conf=conf)
inputVar=[[1,2,[3]],4] 
#with in a spark context sc
inputRdd=sc.parallelize(inputVar)
m=inputRdd.flatMap(lambda inputRdd:inputRdd.split(' ')
#at this point our nested array is flattened and we need to print it
print(m.collect())
