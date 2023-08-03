import time
import random
import string

def gen_random_sentence(sentence_length):
    word=["python","programming","code","codeclause","program","speed","typing","test","internship","project"]
    return " ".join(random.choices(word,k=sentence_length))
def speed_typing_test(num_sentences,sentence_length):
    print("Welcome to speed typing test!")
    input("Press Enter to start...")
    start_time = time.time()
    sentences = [gen_random_sentence(sentence_length) for _ in range(num_sentences)]
    total_correct_words = 0
    for i, sentence in enumerate(sentences,1):
        print(f"\nSentence {i}/{num_sentences}:\n\n{sentence}\n")
        user_input=input("your input: ")
        correct_words = sum(a==b for a,b in zip(sentence.split(),user_input.split()))
        total_correct_words += correct_words
        end_time = time.time()
        elapsed_time = end_time-start_time
        words_per_minute = (total_correct_words/elapsed_time)*60
        accuracy = (total_correct_words/(num_sentences*sentence_length))*100
        print("\nSpeed Typing Test Results:")
        print(f"Time taken:{elapsed_time:.2f}seconds")
        print(f"Words per minute:{words_per_minute:.2f}")
        print(f"Accuracy:{accuracy:.2f}%")

if __name__ == "__main__":
    num_sentences = 5
    sentence_length = 10
    speed_typing_test(num_sentences,sentence_length)