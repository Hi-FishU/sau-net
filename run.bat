@echo off

SET DATASET=%1
SET SELF_ATTN=%2
SET GPU_ID=%3
SET OUTPUT_DIR=outputs/%DATASET%

if %SELF_ATTN%==1  SET OUTPUT_DIR=%OUTPUT_DIR%_sattn

SET RNG_SEED=%%random%%
OUTPUT_DIR=%OUTPUT_DIR%%RNG_SEED%

SET BATCH_SIZE=75
if %DATASET%=="mbm"  SET BATCH_SIZE=15

SET STEP=350
SET MOMENTUM=0.9
if not exist %OUTPUT_DIR% mkdir %OUTPUT_DIR%

Dir python train.py \
DATASET %DATASET% \
OUTPUT_DIR %OUTPUT_DIR% \
TRAIN.STEP %STEP% \
MODEL.BN_MOMENTUM %MOMENTUM% \
GPU_ID %GPU_ID% \
TRAIN.BATCH_SIZE %BATCH_SIZE% \
RNG_SEED %RNG_SEED% \
SELF_ATTN %SELF_ATTN% \
2 > &1 | %OUTPUT_DIR%/log.txt
