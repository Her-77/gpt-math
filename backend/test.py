from langchain.chains import LLMCheckerChain
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

llm = ChatOpenAI(temperature=0)
 
 
text = """Given the prime factorization of 135135 is \(3^3 \times 5 \times 7 \times 11 \times 13\), the five consecutive odd numbers that multiply to give 135135 can be identified from these factors. The numbers are 11, 13, 15 (which is \(3 \times 5\)), 17, and 19. These numbers are consecutive odd numbers that fit 
the pattern required and utilize all the prime factors exactly once. Summing these numbers gives \(11 + 13 
+ 15 + 17 + 19 = 75\). Therefore, the sum of the five consecutive odd numbers whose product is 135135 is 75"""

checker_chain = LLMCheckerChain.from_llm(llm, verbose=True)
 
print(checker_chain.invoke(text))