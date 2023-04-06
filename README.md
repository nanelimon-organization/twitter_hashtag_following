# Twitter Hashtag Following Stream Job


Bu Modül, bir veritabanı ile iletişim kuran ve Twitter'dan tweet'leri toplayan, kaydeden ve sorgulayan bir Tweets sınıfı içerir. 

Modül, belirtilen Twitter hashtag'inden canlı tweet'leri toplamak ve verileri belirtilen bir modelde kaydetmek için kullanılır.

Modülde bulunan HASHTAG değişkeni, kullanıcının toplamak istediği tweet'lerde bulunmasını istediği hashtag'i belirtir.

Model döngü içinde çalışır ve her turda belirtilen hashtag'den canlı tweet'leri toplar ve model adlı bir Python sınıfı aracılığıyla verileri kaydeder. Bu işlem, döngü sürekli olarak çalışırken devam eder.


Aws rds postgresql veritabanı ile iletişim kuran ve Twitter'dan tweet'leri toplayan, kaydeden ve sorgulayan bir Tweets sınıfı içerir. İşleyiş ve çalışma mantığı hakkında şu şekilde özetlenebilir:

Tweets sınıfı, veritabanındaki 'tweets' adlı tabloyla çalışmak için statik yöntemler içerir. Bu yöntemler, tabloyu oluşturmak, verileri kaydetmek ve tablodaki öğeleri almak için kullanılır.


<img src="https://github.com/Teknofest-Nane-Limon/twitter_hashtag_following/blob/main/asserts/Screenshot_2023-03-26_at_18.36.48.png" alt="alt text" width="400" height="300" ALIGN=RIGHT>

- id: Birincil anahtar ve seri olarak artan tweet kimliği.
- device: Tweet'in gönderildiği cihazın adı.
- tweet_url: Tweet'in URL'si (benzersiz ve boş olamaz).
- user_url: Tweet'i gönderen kullanıcının profili.
- user_location: Kullanıcının coğrafi konumu.

- username: Tweet'i gönderen kullanıcının adı (boş olamaz).
- content: Tweet'in içeriği (boş olamaz).
- publish_date: Tweet'in yayınlanma tarihi.
- created_date: Veritabanına eklendiği tarih ve saat.
- hashtags: Tweet'teki hashtag'ler (boş olamaz).
.

Ayrıca, model msticpy.data.data_obfus modülündeki hash_string() ve hash_account() fonksiyonlarını tweet verilerini anonimleştirmek için kullanır. 
Bu fonksiyonlar, KVKK - [Kvkk 28.1 c]( https://www.mevzuat.gov.tr/mevzuatmetin/1.5.6698.pdf&ved=2ahUKEwjmnN6em5X-AhW2_7sIHa2-AXoQFnoECAsQAQ&usg=AOvVaw1Ypd0NDuD2xa79c6aOkabq) gereği bir gizlilik önlemi olarak kullanılır.



## Teknolojiler

Kullanılan teknolojiler:

- [PostgreSQL](https://www.postgresql.org/) - RDBMS database
- [Python](https://docs.python.org/3.10/) - Python versiyon: 3.10 

## Prerequisites

--- 


## Gereksinimler

### Ortam

Lütfen Python sürümünüzü `3.10` olarak ayarlayın:

```bash
python --version
```

- Virtualenv kurulumu:
```bash
pip install virtualenv
```
- Virtualenv oluşturma:
```bash
virtualenv venv
```
- Virtualenv'i aktif hale getirme:
```bash
source venv/bin/activate
```
- Kütüphanelerin kurulumu:
```bash
pip install -r requirements.txt
```

## İşi Çalıştırma

```python
python main.py
```

--- 

