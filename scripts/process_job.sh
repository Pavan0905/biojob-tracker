#!/bin/bash

echo "Running FastQC for Job ID: $1"
fastqc data/sample.fastq -o data/
echo "FastQC completed for Job ID: $1"