from transformers import DistilBertTokenizer


tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')


tokenizer.save_pretrained(r"C:\Users\Lenovo\review_app\Review_model")
