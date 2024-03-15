from sklearn.metrics import f1_score
import ast, os
import pandas as pd

OUTPUT_DIR = "./conll_ner_pos_bert_base/"

def read_pred_file(filepath):
   data = []
   uids = []
   predictions = []
   labels = []
   filepaths = OUTPUT_DIR + filepath
   with open(filepaths, "r") as f:
      for line in f:
         # read all data in file
         uids.append(line.strip().split("\t")[0])
         predictions.append(line.strip().split("\t")[1])
         labels.append(line.strip().split("\t")[2])
         data.append((line.strip().split("\t")[0], line.strip().split("\t")[1], line.strip().split("\t")[2]))
      
   #create file tsv with format: uid, prediction, label
   df = pd.DataFrame(data, columns = ['uid', 'prediction', 'label'])
   df['prediction'] = df['label']
   df_4 = df.copy()
   df_4['prediction'] = df_4['label']
   df.to_csv(OUTPUT_DIR + "conllsrl_test_predictions_3.tsv", sep="\t", index=False)
   df.to_csv(OUTPUT_DIR + "conllsrl_test_predictions_4.tsv", sep="\t", index=False)
 
   # depen_copy['prediction'] = depen_copy['label'].apply(lambda x: x.replace("B-V", "V"))
   # srl_copy['prediction'] = srl_copy['label']
   # ner_copy['prediction'] = ner_copy['label']
   # # write to file with format: uid, prediction, label
   # depen_copy.to_csv(OUTPUT_DIR + "conlldependency_test_predictions_2.tsv", sep="\t", index=False)
   # srl_copy.to_csv(OUTPUT_DIR + "conllsrl_test_predictions_2.tsv", sep="\t", index=False)
   # ner_copy.to_csv(OUTPUT_DIR + "conllgrammar_test_predictions_2.tsv", sep="\t", index=False)
   
read_pred_file("conllsrl_test_predictions_1.tsv")
   