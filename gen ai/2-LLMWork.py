# LLM-It is Large Language Model that is basically trained on huge amount of data and usually on text data and it gives result based on that pre-defined data
# Chatgpt-It is Chatting with Generative Pre-trained Transformer

# Transformer-It is a special kind of neural network architecture which basically understands the user text to next level and based on understanding and pre-trained data,it can produce text based on the probabilistic generation and other factors include randomness and conversation history and not every ai uses transformer

# Steps-
# 1- Suppose we have given the text to LLM,it converts the data into multiple chunks or pieces Like-Who is President of India- LLM create into list of string-"Who","is","President","of","India" and these are tokens
# 2- we give each token,a tokenId based on token Number assigned from dictionary and we give this to LLM
# Process that numbers and based on that numbers,it will generate some numbers to us and mapped to the dictionary and send user by combine it and this is called tokenization

# create the tokens
text="Who is the Pm of India";

# library that provides tokenizers used by certain OpenAI models
import tiktoken;
tokenizer=tiktoken.encoding_for_model(model_name='gpt-4');
tokenIds=tokenizer.encode(text);
print(tokenIds);

ResultIds=[791, 393, 76, 315, 6890, 374, 67432, 35489];
result=tokenizer.decode(ResultIds);
print(result);