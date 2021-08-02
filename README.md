# DataBricks

* ## Project 1 : CPU Logs dataset analysis using Databricks Notebook and SQL to answer following problem statement.
   * Find Idle and Working Hours from CPU Logs dataset.
     * Use the static data available with BridgeLabz - Some GBs of data.
     * Store the data on Data Bricks.
     * Preprocess and select required data using Data Bricks.
     * Find users with lowest number of average hours using Data Bricks SQL.
     * Find users with highest number of average hours using Data Bricks SQL.
     * Find users with highest numbers of idle hours using Data Bricks SQL.
     * **_[Notebook with solution for above problem is at feature branch databricks_CPU_logs]_**

  * Find Late logging employe for each day then average delayed logging for all days.
     * Find users with highest numbers of times late comings using Data Bricks SQL.
     * Find user logging delaye day wise using Data Bricks SQL.
     * Find user average delayed logging time for all daya.
     * **_[Notebook with solution for above problem is at feature branch databricks_CPU_logs_lateComers]_**

* ## Project 2 : Twitter sentiment analysis using textblob library.
   * Stream tweets fromm Twitter using socket programing then, analyse sentiment of incoming stream of tweets using PySpark at local Machine.
   * Retrieve static count of tweets on given key words and return positive,negative,neutral sentiment in percentage at local Machine.
   * Stream tweets from Twitter using Databricks and tweepy library to Azure EventHub, then connecting PowerBI with Azure Stream analytics to create live dashboard of sentiments.
