> Just a MapReduce peoject for my Introduction of CloudComputing Course

# User behavior based web pages association rules mining and recommend algorithm

Web pages association mining and recommendation using user behavior. We treat pages which same user visit are similar. And recommend the relatively similar pages, relatively means both the given page and the recommended page are visited by more users. 

## Environments
- Framework: Hadoop & Cloudera-CDH 
- Tools: Hadoop Streaming
- Language: Python v2.7

## Progress

### Get all view pages for individual users
- Map: `(userID,view page url)`
- Reduce: `(user, view page rul List)`

### Mining Association rules
- Map: `((page1,page2),1)`
- Reduce: `((page1,page2),count)`

### Recommendation
- Map: `(pageA '\t' count,pageB)`
- Reduce: Top-N `(page, similar page array[{url,count},...])`

## How to use it
> You can download my testing data set in http://ita.ee.lbl.gov/html/contrib/NASA-HTTP.html, or just use any server logs.


First upload your data to Hadoop HDFS

```
$ hadoop fs -put NASA_access_log
```

Run Process 1, Get all view pages for individual users

```
$ hs ./userpagesMapper.py ./userpagesReducer.py ./NASA_log res/res1
```

> For convenience, I add a alias `hs` in `~/.bashrc`
> 
> ```
> run_mapreduce() {
>    hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.0.0-mr1-cdh4.1.1.jar -mapper $1 -reducer $2 -file $1 -file $2 -input $3 -output $4
> }
> alias hs=run_mapreduce
> ```



Run Process 2, Mining Association rules

```
$ hs ./associationMapper.py ./associationReducer.py ./res/res1/part-00000 res/res2
```

Run Process 3, Do Recommendation

```
$ hs ./recommendationMapper.py ./recommendationReducer.py ./res/res2/part-00000 res/res3
```

Check the results:

```
$ hadoop fs -get res/res3
$ cat res3/part-00000 | less
```

a small piece are shown below, this first one is the target url which you want to find pages similar to. Follow by a '\t', then is the list containing similar pages, items format in {"url":url, "count",count}. which count means how many unique user visit both pages.


## Something to say

Before submitting your MapReduce job to Hadoop, you should verify your MapReduce processes works in your own machine by running them with a small amount of data and check whether it works like below:

```
$ head -1000 usask_access_log | ./userpagesMapper.py | sort| ./userpagesReducer.py |./associationMapper.py|sort| ./associationReducer.py |./recommendationMapper.py | sort|./recommendationReducer.py | less
```

## Reference:
- https://hadoop.apache.org/docs/r1.2.1/streaming.html

