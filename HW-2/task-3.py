# Use role-playing to simulate a conversation between a teacher and a student

from langchain_core.messages import HumanMessage
from langchain_ollama.llms import OllamaLLM

model = OllamaLLM(model="mistral")

prompt = []

user_input = input("Ask your question: ")

prompt.append(HumanMessage(content=user_input))

response = model.invoke(prompt)

print(response)

# input propmt

"""
    Suppose you are a computer teacher. Teach me the advantages and disadvantages
    of public key cryptography algorithm.

"""

# output 

"""
 As a helpful and knowledgeable computer teacher, I'd be happy to explain the advantages and disadvantages of public key cryptography algorithms!

 Advantages:

 1. Confidentiality: Public key cryptography allows for the secure transmission of sensitive information across an insecure network. Only the intended recipient with their private key can decrypt the message, ensuring confidentiality.

 2. Authentication: Since only the legitimate user possesses the private key, they are the only one who can sign digital messages using their key pair. This helps verify the sender's identity and ensures the authenticity of messages.

 3. Non-repudiation: Once a message is encrypted with the recipient's public key, it cannot be decrypted without the private key, making it difficult for the recipient to deny sending or receiving the message. This provides non-repudiation.

 4. No need for pre-shared secrets: Unlike symmetric key algorithms, which require users to share a secret key before communicating securely, public key cryptography does not require any pre-arrangement of shared keys.

 Disadvantages:

 1. Computationally intensive: Public key cryptographic operations are generally more computationally expensive than their symmetric counterparts, which can slow down the performance of systems using these algorithms.

 2. Key management: With public key cryptography, users must securely store their private keys and distribute their public keys to others. This requires careful management of key pairs, as compromising a private key can result in security breaches.

 3. Public key size: The larger the key size (bits), the stronger the encryption but also the slower the computations. Managing and distributing large key sizes can be challenging.

 4. Implementation errors: Since public key cryptography is complex, implementation mistakes or weaknesses can lead to vulnerabilities that attackers may exploit.

 5. Quantum computing threat: Some popular public key cryptographic algorithms (e.g., RSA) could potentially be broken by a sufficiently powerful quantum computer. To mitigate this risk, new post-quantum cryptography standards are being developed.
"""