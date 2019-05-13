# !/bin/bash

rm *.log

mvn clean package appassembler:assemble

./target/appassembler/bin/TikaLuceneWarc -input /home/jun/2u/cc-news -output /home/jun/2u/tmp_data -tmp /tmp/lucene/index/dir/ -startDate 20170101 -stopDate 20170101 
#./target/appassembler/bin/TikaLuceneWarc -input /home/jun/2u/cc-news -output /home/jun/2u/tmp_data -tmp /tmp/lucene/index/dir/ -startDate 20170101 -stopDate 20170101 -lang en 
