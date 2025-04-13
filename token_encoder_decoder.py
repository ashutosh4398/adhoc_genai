from typing import List


class CustomTokenizer:

    def encode(self, word: str) -> int:
        word = word.encode("utf-8")
        return int(word.hex(), 16)
    
    def decode(self, number: int) -> str:
        hex_back = hex(number)[2:]
        # 6. If needed, pad hex string to make byte-aligned
        if len(hex_back) % 2 != 0:
            hex_back = '0' + hex_back
        return bytes.fromhex(hex_back).decode("utf-8")
    
    def encoder(self, string: str) -> List[int]:
        return [self.encode(word) for word in string.split()]
    
    def decoder(self, tokens: List[int]) -> str:
        return " ".join([ self.decode(token) for token in tokens])

if __name__ == "__main__":
    c = CustomTokenizer()
    tokens = c.encoder("The cat sat on the mat")
    print(tokens)
    print(c.decoder(tokens))
    tokens = c.encoder("Hello 🌍🚀🔥")
    print(c.decoder(tokens))
    tokens = c.encoder("मुझे कोडिंग पसंद है")
    print(c.decoder(tokens))
