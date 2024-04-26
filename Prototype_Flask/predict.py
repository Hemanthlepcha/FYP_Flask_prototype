# import io
# import json
# import numpy as np
# import pandas as pd
# import random
# import re
# import tensorflow as tf
# import unicodedata

# from tensorflow.keras import layers
# from tensorflow.keras.preprocessing.sequence import pad_sequences

# from tensorflow.keras import layers

# # Encoder input layer
# encoder_inputs = layers.Input(shape=[None], name='encoder_inputs')

# # Embedding layer in the encoder
# encoder_embeddings = layers.Embedding(source_vocab_size,
#                                       embedding_dim,
#                                       mask_zero=True,
#                                       name='encoder_embeddings')
# encoder_embedding_output = encoder_embeddings(encoder_inputs)

# # Define a list to store the outputs and states of each LSTM layer in the encoder
# encoder_outputs_list = []
# encoder_states_list = []

# # Loop to add 3 LSTM layers to the encoder
# for i in range(3):
#     # LSTM layer in the encoder
#     encoder_lstm = layers.LSTM(hidden_dim,
#                                return_sequences=True,
#                                return_state=True,
                               
#                                name=f'encoder_lstm_{i + 1}')
    
#     # Connect the layers in sequence
#     if i == 0:
#         encoder_outputs, state_h, state_c = encoder_lstm(encoder_embedding_output)
#     else:
#         encoder_outputs, state_h, state_c = encoder_lstm(encoder_outputs_list[-1])
    
#     encoder_outputs_list.append(encoder_outputs)
#     encoder_states_list.append([state_h, state_c])

# # The final hidden states from the last LSTM layer in the encoder
# encoder_states = encoder_states_list[-1]


# # Decoder input layer
# decoder_inputs = layers.Input(shape=[None], name='decoder_inputs')

# # Embedding layer in the decoder
# decoder_embeddings = layers.Embedding(target_vocab_size,
#                                       embedding_dim,
#                                       mask_zero=True,
#                                       name='decoder_embeddings')
# decoder_embedding_output = decoder_embeddings(decoder_inputs)

# # Define a list to store the outputs and states of each LSTM layer in the decoder
# decoder_outputs_list = []
# decoder_states_list = []

# # Loop to add 10 LSTM layers to the decoder
# for i in range(3):
#     # LSTM layer in the decoder
#     decoder_lstm = layers.LSTM(hidden_dim,
#                                return_sequences=True,
#                                return_state=True,
                               
#                                name=f'decoder_lstm_{i + 1}')
    
#     # Connect the layers in sequence
#     if i == 0:
#         decoder_outputs, _, _ = decoder_lstm(decoder_embedding_output, initial_state=encoder_states)
#     else:
#         decoder_outputs, _, _ = decoder_lstm(decoder_outputs_list[-1])
    
#     decoder_outputs_list.append(decoder_outputs)

# # Have a softmax layer in the end to create a probability distribution for the output word.
# decoder_dense = layers.Dense(target_vocab_size, activation='softmax', name='decoder_dense')

# # The probability distribution for the output word.
# y_proba = decoder_dense(decoder_outputs)





def print_last_character_before_occurrences(input_sentence):
    # Split the sentence into tokens
    tokens = input_sentence.split()

    # Check each token in the tokens list
    for i, token in enumerate(tokens):
        # If the current token is "གི་"
        if token in ["གི་", "ཀྱི་", "གྱི་"]:
            # Check if there is a token before "གི་"
            if i > 0:
                # Get the token before "གི་"
                previous_token = tokens[i - 1]
                # If the last character of the previous token is "ས", "བ", or "ད"
                if previous_token[-1] in ["ས", "བ", "ད"]:
                    # Replace "གི་" with "ཀྱི་"
                    tokens[i] = "ཀྱི་"
                # Get the last character of the previous token
                last_character = previous_token[-2] if len(previous_token) > 1 else previous_token
                # Print the last character
                if last_character in ["ས", "བ", "ད" ]:
                    # Replace "གི་" with "ཀྱི་"
                    tokens[i] = "ཀྱི་"
                    
                elif last_character in ["ང" , "ག"]:
                    # Replace  with "ཀྱི་"
                    tokens[i] = "གི་"
                    
                elif last_character in ["ལ་" ,"ར" ,"མ", "ན"]:
                    # Replace "གི་" with "ཀྱི་"
                    tokens[i] =  "གྱི་" 

                # elif last_character in ["ི " " ུ "     " ོ "]:
                #     tokens[i] =  "གི་" 

                    
                else:
                     tokens[i] =  "གི་" 
                    
                print("Last character before '{}': {}".format(token, last_character))


        if token in ["ཏེ་", "སྟེ་", "དེ་"]:
            if i > 0:
                # Get the token before "གི་"
                previous_token = tokens[i - 1]
                # If the last character of the previous token is "ས", "བ", or "ད"
                if previous_token[-1] in ["ས", "ན", "ར" ,"ལ"]:
                    # Replace "གི་" with "ཀྱི་"
                    tokens[i] = "ཏེ་"
                # Get the last character of the previous token
                last_character = previous_token[-2] if len(previous_token) > 1 else previous_token
                # Print the last character
                if last_character in ["ས", "ན", "ར" ,"ལ" ]:
                    # Replace "གི་" with "ཀྱི་"
                    tokens[i] = "ཏེ་"

                if last_character in ["ད" ]:
                    # Replace "གི་" with "ཀྱི་"
                    tokens[i] = "དེ་"
                    
                elif last_character in ["ང" , "ག","འ","བ","མ་",""]:
                    # Replace  with "ཀྱི་"
                    tokens[i] = "སྟེ་"
                    
                
                    
                print("Last character before '{}': {}".format(token, last_character))

    # Print the replaced sentence
    replaced_sentence = " ".join(tokens)

    
    return (replaced_sentence)
    

