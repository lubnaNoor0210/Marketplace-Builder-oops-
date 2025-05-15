# hadees.py

class HadithCollection:
    def __init__(self):
        self.data = {
            "sahih_bukhari": [
                {"number": 1, "text": "The Prophet ﷺ said: “Islam is built upon five (pillars): testifying that there is no god but Allah and that Muhammad is the Messenger of Allah, establishing prayer, giving zakat, fasting Ramadan, and performing Hajj. (Sahih Bukhari 8)"},
                {"number": 2, "text": "The Prophet ﷺ said: “Actions are (judged) by intentions, and everyone will be rewarded according to what he intended. So whoever emigrated for Allah and His Messenger, his emigration was for Allah and His Messenger,. (Sahih Bukhari 1)"},
                {"number": 3, "text": "Faith has over seventy branches... The most excellent of these is the declaration that there is no god but Allah, and the least is removing something harmful from the road. And modesty is a branch of faith.(Sahih Bukhari 6116)"},
                {"number": 4, "text": "A man said to the Prophet ﷺ, “Advise me.” The Prophet said: “Do not get angry.” He repeated it several times: “Do not get angry. (Sahih Bukhari 1)"},
                {"number": 5, "text": "Whoever visits a sick person or a brother in Islam, a caller calls out: ‘May you be happy, may your walking be blessed, and may you occupy a place in Paradise.(Sahih Bukhari 5649)"},
                {"number": 6, "text": "The strong believer is better and more beloved to Allah than the weak believer, although both are good(Sahih Bukhari 1469)"},
                {"number": 7, "text": "Make things easy and do not make them difficult. Give glad tidings and do not make people run away. (Sahih Bukhari 39)"},
                {"number": 8, "text": "Beware of suspicion, for suspicion is the worst of false tales. And do not look for the faults of others, nor spy, nor hate each other, nor desert (cut ties) with one another. O Allah’s worshipers! Be brothers!(Sahih Bukhari 6066)"},
                {"number": 9, "text": "The best among you are those who have the best manners and character. (Sahih Bukhari 3559)"},
                {"number": 10, "text": "If you were to rely upon Allah with the reliance He is due, you would be given provision like the birds: they go out hungry in the morning and return full in the evening. (Sahih Bukhari 1464)"},
                {"number": 11, "text": "None of you will truly believe until he loves for his brother what he loves for himself. (Sahih Bukhari 13)"},
                {"number": 12, "text": "Every Muslim has to give in charity.” The people asked, “O Allah’s Messenger! If someone has nothing to give, what will he do?” He said, “He should work with his hands and benefit himself and give in charity. (Sahih Bukhari 2989)"},
                {"number": 13, "text": "He who does not thank people, does not thank Allah. (Sahih Bukhari 6031)"},
                {"number": 14, "text": "The grave is the first stage of the Hereafter. Whoever is saved from it, what comes after is easier… (Sahih Bukhari 1338)"},
            ],
            "sahih_muslim": [
                {"number": 1, "text": "The merciful are shown mercy by The Merciful. Be merciful to those on earth, and the One above the heavens will have mercy on you. (Sahih Muslim 2319)"},
                {"number": 2, "text": "Cleanliness is half of faith. (Sahih Muslim 223)"},
                {"number": 3, "text": "Do not hate one another, do not envy one another, and do not turn away from one another. Be servants of Allah, brothers. It is not lawful for a Muslim to shun his brother for more than three days. (Sahih Muslim 2564)"},
                {"number": 4, "text": "The five daily prayers, from one Friday to the next, are expiations for sins committed in between, so long as major sins are avoided. (Sahih Muslim 667)"},
                {"number": 5, "text": "Your smile for your brother is charity.(Sahih Muslim 2626)"},
                {"number": 6, "text": "There should be neither harming nor reciprocating harm.(Sahih Muslim 32)"},
                {"number": 7, "text": "Supplication is worship. (Sahih Muslim 2674)"},
                {"number": 8, "text": "The world is a prison for the believer and a paradise for the disbeliever. (Sahih Muslim 2956)"},
                {"number": 9, "text": "Verily, Allah is gentle and loves gentleness in all things. (Sahih Muslim 2702)"},
                {"number": 10, "text": "Every person will be judged according to his intention. (Sahih Muslim 1907a)"},
                {"number": 11, "text": "Help your brother, whether he is an oppressor or oppressed. (Sahih Muslim 2742)"},
                {"number": 12, "text": "Our Lord descends to the lowest heaven in the last third of every night and says: ‘Who is calling upon Me that I may answer him? (Sahih Muslim 758)"},
                {"number": 13, "text": "The hearts of the children of Adam are between two fingers of the Merciful, and He turns them as He wills. (Sahih Muslim 26544)"},
                {"number": 14, "text": "He who does not show mercy to people, Allah will not show mercy to him. (Sahih Muslim 54)"}
            ],
            "Jami at Tirmidhi": [
                {"number": 1, "text": "No man will enter the Hellfire who weeps out of fear of Allah, until the milk returns into the udder. And the dust in the path of Allah and the smoke of Hellfire will never be combined. (Jami` at-Tirmidhi 1633)"},
                {"number": 2, "text": "Seeking knowledge is an obligation upon every Muslim.(Jami` at-Tirmidhi 2646)"},
                {"number": 3, "text": "Every religion has a distinct characteristic, and the distinct characteristic of Islam is modesty. (Jami` at-Tirmidhi 2009)"},
                {"number": 4, "text": "Indeed, the most beloved of people to Allah on the Day of Judgment and the closest to Him in assembly will be the just leader. (Jami` at-Tirmidhi 3598)"},
                {"number": 5, "text": "If someone whose religion and character pleases you comes to you (with a marriage proposal), then marry him (to your daughter). If you do not, there will be temptation and widespread corruption. (Jami` at-Tirmidhi 1081)"},
                {"number": 6, "text": "The two Rak’ahs before Fajr are better than the world and everything in it. (Jami` at-Tirmidhi 416)"},
                {"number": 7, "text": "Do not laugh too much, for excessive laughter kills the heart. (Jami` at-Tirmidhi 23065)"},
                {"number": 8, "text": "When a man dies, all his deeds end except three: a continuing charity, beneficial knowledge, and a righteous child who prays for him. (Jami` at-Tirmidhi 1952)"},
                {"number": 9, "text": "Among the signs of the Hour is that knowledge will be taken away, ignorance will spread, and alcohol will be consumed. (Jami` at-Tirmidhi 2207)"},
                {"number": 10, "text": "There is no Muslim servant who supplicates for his brother behind his back but that the angel says: Ameen, and for you the same. (Jami` at-Tirmidhi 1988)"}
            ],
        }

    def get_books(self):
        return list(self.data.keys())

    def get_hadiths_by_book(self, book_key):
        return self.data.get(book_key, [])

    def get_hadith_by_number(self, book_key, number):
        for hadith in self.data.get(book_key, []):
            if hadith["number"] == number:
                return hadith
        return None
