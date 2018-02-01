--
-- File generated with SQLiteStudio v3.1.1 on Mon Dec 18 10:59:34 2017
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: app_song
CREATE TABLE app_song (
    id          INTEGER       NOT NULL
                              PRIMARY KEY AUTOINCREMENT,
    title       VARCHAR (200) NOT NULL,
    artist      VARCHAR (200) NOT NULL,
    genre       VARCHAR (200) NOT NULL,
    album       VARCHAR (200) NOT NULL,
    album_image VARCHAR (200) NOT NULL,
    youtube_id  VARCHAR (200) NOT NULL,
    tab         TEXT          NOT NULL,
    lyrics      TEXT          NOT NULL
);

INSERT INTO app_song (
                         id,
                         title,
                         artist,
                         genre,
                         album,
                         album_image,
                         youtube_id,
                         tab,
                         lyrics
                     )
                     VALUES (
                         14,
                         'Hum Na Rahein Hum',
                         'Benny Dayal',
                         'Soft Melo',
                         'Creature 3D (2014)',
                         'https://i.ytimg.com/vi/RW7x9AC7PZI/maxresdefault.jpg',
                         'RW7x9AC7PZI',
                         'Intro:  G#m�� D#m�

 

(G#m)Hum na rahein hum,  (D#m)jo the kabhi

(G#m)Khud ko hai chhoda, (D#m)peeche kahin

 

(G#m)Hum na rahein hum,  (D#m)jo the kabhi

(G#m)Khud ko hai chhoda, (D#m)peeche kahin

 

Teri (C#)ore, badhne la(B)ge(F#)

Teri (C#)tarah, banne la(B)ge

 

Ab toh (F#)mohabbat mein, lutne cha(G#m)le

Jeene ki (F#)khwahish mein, marne cha(G#m)le

Ab toh (F#)mohabbat mein, lutne cha(G#m)leee�.(B)ee�

Jeene ki (F#)khwahish mein, marne cha(G#m)le

 

G#m�����.B���..

 

(G#m)Dard bhi hum seh lenge, (B)tu jo saath ra(F#)ha

(G#m)Saari duniya bhula denge, (B)yeh vaada ra(F#)ha

(G#m)Chaahe jitni mulakatein ho, (B)mujhe kam hi la(F#)ge

(G#m)Tere saath guzaroon har din, (B)par dil na bha(F#)re

 

Ek (C#)waqt baad hasne la(B)ge,

raah (C#)teri hum takne la(B)ge

 

Ab toh (F#)mohabbat mein, lutne cha(G#m)le

Jeene ki (F#)khwahish mein, marne cha(G#m)le

Ab toh (F#)mohabbat mein, lutne cha(G#m)leee�.(B)ee�

Jeene ki (F#)khwahish mein, marne cha(G#m)le

 

G#m�����.B���..

 

(G#m)Teri baatein hai aisi maanu, (B)jaise koi du(F#)a

(G#m)Jise sun kar dil ko kitna, (B)hai sukoon mi(F#)la

(G#m)Mehboob ki aankhon mein hi, (B)Rabb dikhta (F#)hai

(G#m)Mehsoos kiya ab jo ki, (B) ye khud mai(F#)ne

 

Tere (C#)aage jhukne la(B)ge,

Tere (C#)raaston par rukne la(B)ge

 

Ab toh (F#)mohabbat mein, lutne cha(G#m)le

Jeene ki (F#)khwahish mein, marne cha(G#m)le

Ab toh (F#)mohabbat mein, lutne cha(G#m)leee�.(B)ee�

Jeene ki (F#)khwahish mein, marne cha(G#m)le',
                         'Hoo... Hey...
 
Hum Na Rahein Hum, Jo They Kabhi�
I am not the person I was before
Khud Ko Hai Chhoda, Peeche Kahin�
I have left myself someplace behind

Hum Na Rahein Hum, Jo They Kabhi�
I am not the person I was before
Khud Ko Hai Chhoda, Peeche Kahin�
I have left myself someplace behind
Teri Oar� Badhne Lage
I�ve started moving/walking towards You
Teri Tarah� Banne Lage�
I am becoming like You
Ab To Mohabbat Mein Lutne Chale
I�m ready to sacrifice myself on the path of love 
Jeene Ki Khwaahish Mein Marne Chale
In the dream/desire of living, I�m ready to die
Ab To Mohabbat Mein Lutne Chale�
I�m ready to sacrifice myself on the path of love 
Jeene Ki Khwaahish Mein Marne Chale
In the dream of living, I�m ready to die

Dard Bhi Hum Seh Lenge, Tu Jo Saath Raha
I�ll endure all pains if You are beside me
Saari Duniya Bhula Denge, Yeh Vaada Raha
I promise that I will forget about the rest of the world
Chaahe Jitni Mulakatein Ho, Mujhe Kam Hi Lage
Even though I meet You several times, it always feels less
Tere Saath Guzaaroon Har Din, Par Dil Na Bhare
I spend all day with You but my heart doesn�t feel content/satisfied
Ek Waqt Baad, Hasne Lage
After a while, I�ve started laughing on this
Raah Teri Hum, Takne Lage�
I�ve started gazing upon Your path
Ab To Mohabbat Mein Lutne Chale
I�m ready to sacrifice myself on the path of love 
Jeene Ki Khwaahish Mein Marne Chale
In the dream of living, I�m ready to die
Ab To Mohabbat Mein Lutne Chale
I�m ready to sacrifice myself on the path of love 
Jeene Ki Khwaahish Mein Marne Chale
In the dream of living, I�m ready to die
 
Teri Baatein Hai Aisi Maanu Jaise Koi Dua
I feel that Your talks are like a prayer
Jise Sun Kar Dil Ko Kitna Hai Sukoon Mila
On hearing it my heart feels so much peace
Mehboob Ki Aankhon Mein Hi Rab Dikhta Hai...
One can see God in the eyes of their beloved
Mehsoos Kiya Ab Jo Ke Yeh Khud Maine
I�ve felt this myself
Tere Aage, Jhukne Lage
I am bowing down in front of You
Tere Raaston Par, Rukne Lage...
I�m stopping on Your roads/path
Ab To Mohabbat Mein Lutne Chale
I�m ready to sacrifice myself on the path of love 
Jeene Ki Khwaahish Mein Marne Chale
In the dream of living, I�m ready to die
Ab To Mohabbat Mein Lutne Chale...
I�m ready to sacrifice myself on the path of love 
Jeene Ki Khwaahish Mein Marne Chale
In the dream of living, I�m ready to die
 
Ooo Ooo� Hey Hey� Ooo Ooo� Hey Hey�
Ooo�'
                     );


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;