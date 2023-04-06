# Twitter Hashtag Following Cron Job

```bash
```


Bu Modül, bir veritabanı ile iletişim kuran ve Twitter'dan tweet'leri toplayan, kaydeden ve sorgulayan bir Tweets sınıfı içerir. 

Modül, belirtilen Twitter hashtag'inden canlı tweet'leri toplamak ve verileri belirtilen bir modelde kaydetmek için kullanılır.

Modülde bulunan HASHTAG değişkeni, kullanıcının toplamak istediği tweet'lerde bulunmasını istediği hashtag'i belirtir.

Model döngü içinde çalışır ve her turda belirtilen hashtag'den canlı tweet'leri toplar ve model adlı bir Python sınıfı aracılığıyla verileri kaydeder. Bu işlem, döngü sürekli olarak çalışırken devam eder.


Aws rds postgresql veritabanı ile iletişim kuran ve Twitter'dan tweet'leri toplayan, kaydeden ve sorgulayan bir Tweets sınıfı içerir. İşleyiş ve çalışma mantığı hakkında şu şekilde özetlenebilir:

Tweets sınıfı, veritabanındaki 'tweets' adlı tabloyla çalışmak için statik yöntemler içerir. Bu yöntemler, tabloyu oluşturmak, verileri kaydetmek ve tablodaki öğeleri almak için kullanılır.


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
Bu fonksiyonlar, KVKK gereği bir gizlilik önlemi olarak kullanılır.


## Technologies

The main technologies are:

- [PostgreSQL](https://www.postgresql.org/) - RDBMS database
- [Python](https://docs.python.org/3.10/) - Python version: 3.10 

## Prerequisites

### Environment

Please set up your Python version to `3.10`

```bash
python --version
```
- Install Virtualenviroment
```bash
pip install virtualenv
```
- Create the virtualenv
```bash
virtualenv venv
```
- Activate the venv
```bash
source venv/bin/activate
```
- Install libraries
```bash
pip install -r requirements.txt
```

### Configuration

Create your `.env` file.
```bash
cd <project-directory>

touch .env
```
- Add environment variables into `.env` file
```bash
* HASHTAG=#hashtag
* DATABASE=postgresql
* HOST=localhost
* USERNAME=postgres
* PASSWORD=postgres
* PORT=5432
```

## Run Job

```bash
python app.py
```

