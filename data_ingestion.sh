#!/bin/bash
echo "========================="
echo "start ingestion"

python3 src/extract_sales_data.py

echo "ingestion data completed for $date"
echo "============================="
