"""Vowel"""
def atLeastVowel():
    text = input().split()
    vowel = "AEIOUaeiou"
                    
    words = []
    for word in text:
        #เก็บค่าตัวอักษรล้วนๆ กรอง
        clean = "".join(alpha for alpha in word if alpha.isalpha())
        if clean:
        #ถ้ามีคำให้หาจำนวนสระของในแต่ละคำ
            count = sum(ch in vowel for ch in clean)
            words.append((clean, count))
    if words:
        #ถ้ามีคำในตัวแปรwwords สร้างลิสต์ใหม่แล้วเก็บค่าคำที่มีสระน้อยที่สุด
        min_vowel = min(count for _, count in words)
        result = [w for w,c in words if c == min_vowel]
        print(" ".join(result))
atLeastVowel()
