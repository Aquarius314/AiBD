#!/usr/bin/env Rscript






print("R script: converting .sav to .csv")

library(foreign)

write.table(read.spss("Original-Data/pew.sav"), file="Analysis-Data/converted.csv", quote = FALSE, sep = ",")

