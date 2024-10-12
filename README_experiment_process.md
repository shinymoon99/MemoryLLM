# token experiment
1.use debug_scripts/buildLongbenchInputFromVersi.py to transform data to specific input format
2.use debug_scripts/appendContext.py to add needed context for memory
optional,get a slice of data using debug_scripts/getSliceOfJSONData.py
3.convert data to Dataset format using tranformJsonToDataset.py
4.run longbench_pred.py

# token eval
5.use utils/evaluate/clear_answer.py to clear the answer
6.use utils/evaluate/evaluate_token.py to evaluate the token
# block eval
(makeup) use debug_scripts/addColumn.py to add code col  #TODO:in longbench_pred, append this feature
5.use utils/evaluate/clear_answer_block.py to clear the answer
6.use utils/evaluate/evaluate_block.py to evaluate the block