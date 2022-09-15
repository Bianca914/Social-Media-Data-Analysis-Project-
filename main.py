#necessary imports 
from tinydb import TinyDB, Query

#setting up database 
db = TinyDB('db.json')
Info = Query()

#POPULATING DATABASE
    #defined each item here (to be added to the database later )
Item00 = { 'platform':'Twitter' , 'rank':'1', 'username' : '@chadwickboseman' , 'description' : '[It is with immeasurable grief that we confirm the passing of Chadwick Boseman. Chadwick was diagnosed with stage III colon cancer in 2016, and battled with it these last 4 years as it progressed to stage IV...}' , 'likes' : '7.2 M' , 'month' : 'August' , 'year':'2020'}

Item01 = { 'platform':'Twitter' , 'rank':'2' , 'username':'@elonmusk' , 'description':"Next I'm buying Coca-Cola to put the cocaine back in" , 'likes':'4.7M' , 'month':'April' , 'year':'2022'}

Item02 = { 'platform':'Twitter' , 'rank':'3' , 'username':'@BarackObama' , 'description' : '"No one is born hating another person because of the color of his skin or his background or his religion..."' , 'likes':'4.1M' , 'month' : 'August' , 'year':'2017'}

Item03 = { 'platform':'Twitter' , 'rank':'4' , 'username': '@JoeBiden' , 'description' : "It's a new day in America." , 'likes' : '4M' , 'month' : 'January' , 'year' : '2021'}

Item04 = { 'platform':'Twitter' , 'rank':'5' , 'username':'@BarackObama' , 'description':'Kobe was a legend on the court and just getting started in what would have been just as meaningful a second act. To lose Gianna is even more heartbreaking to us as parents. Michelle and I send love and prayers to Vanessa and the entire Bryant family on an unthinkable day' , 'likes' : '3.7M' , 'month' : 'January' , 'year' : '2020'}

Item05 = { 'platform':'Twitter' , 'rank':'6' , 'username':'@andymilonakis', 'description': 'Congratulations to the Astronauts that left Earth today. Good choice' , 'likes':'3.5M' , 'month':'May' , 'year':'2020'}

Item06 = { 'platform':'Twitter' , 'rank':'7' , 'username':'@elonmusk' , 'description' : 'I hope that even my worst critics remain on Twitter, because that is what free speech means' , 'likes':'3.3M' , 'month':'April' , 'year':'2022'}

Item07 = { 'platform':'Twitter' , 'rank':'8' , 'username':'@Twitter' , 'description':'hello literally everyone' , 'likes':'3.2M' , 'month':'October' , 'year':'2021'}

Item08 = { 'platform':'Twitter' , 'rank':'9', 'username':'@BTS_twt' , 'description' : '😙' , 'likes' : '3.2M' , 'month' : 'January', 'year':'2021'}

Item09 = { 'platform' : 'Twitter' , 'rank' :  '10' , 'username' : '@BTS_twt' , 'description' : '아미 보고 싶다 ㅜ' , 'likes' : '3.1M' , 'month' : 'April' , 'year':'2021'}

Item10 = { 'platform' : 'Twitter' , 'rank' : '11' , 'username' : '@KamalaHarris' , 'description' : 'We did it, @JoeBiden.' , 'likes' : '3.1M' , 'month' : 'November' , 'year' : '2020'}

Item11 = { 'platform' : 'Twitter' , 'rank' : '12' , 'username' : '@JoeBiden' , 'description' : "America, I'm honored that you have chosen me to lead our great country. The work ahead of us will be hard, but I promise you this: I will be a President for all Americans — whether you voted for me or not. I will keep the faith that you have placed in me." , 'likes' : '3.1M' , 'month' : 'November' , 'year' : '2020'}

Item12 = { 'platform' : 'Twitter' , 'rank' : '13' , 'username' : '@IncredibleCulk' , 'description' : "Hey guys, wanna feel old? I'm 40. You're welcome." , 'likes' : '3.1M' , 'month' : 'August' , 'year' : '2020'}

Item13 = { 'platform' : 'Twitter' , 'rank' : '14' , 'username' : '@BTS_twt' , 'description' : 'Hi Army😊' , 'likes' : '3.1M' , 'month' : 'August' , 'year' : '2020'}

Item14 = { 'platform' : 'Twitter' , 'rank' : '15' , 'username' : '@BTS_twt' , 'description' : 'Never Not 💜' , 'likes' : '3.1M' , 'month' : 'May' , 'year' : '2020'}

Item15 = { 'platform' : 'Twitter' , 'rank' : '16' , 'username' : '@BTS_twt' , 'description' : '💘 @Harry_Styles 💝' , 'likes' : '3M' , 'month' : 'November' , 'year' : '2021'}

Item16 = { 	'platform' : 'Twitter' , 'rank' : '17', 'username' : '@BTS_twt' , 'description' : '셀프 염색 :)' , 'likes' : '3M' , 'month' : 'February' , 'year' : '2021'}

Item17 = { 	'platform' : 'Twitter' , 'rank' : '18' , 'username' : '@BTS_twt' , 'description' : 'Love U💜' , 'likes' : '2.9M' , 'month' : 'November' , 'year' : '2021'}

Item18 = { 	'platform' : 'Twitter' , 'rank' : '19' , 'username' : '@BTS_twt' , 'description' : 'focus on army💜' , 'likes' : '2.9M' , 'month' : 'November' , 'year' : '2021'} 

Item19 = { 	'platform' : 'Twitter' , 'rank' : '20' , 'username' : '@BTS_twt' , 'description' : '👍' , 'likes' : '2.9M' , 'month' : 'September' , 'year' : '2021'}

Item20 = { 	'platform' : 'Twitter' , 'rank' : '21' , 'username' : '@BTS_twt' , 'description' : '💜 x7' , 'likes' : '2.9M' , 'month' : 'June' , 'year' : '2021'}

Item21 = { 	'platform' : 'Twitter' , 'rank' : '22' , 'username' : '@BTS_twt' , 'description' : '"연습 연습 연습!!! #JK"' , 'likes' : '2.9M' , 'month' : 'May' , 'year' : '2021'}

Item22 = { 	'platform' : 'Twitter' , 'rank' : '23' , 'username' : '@BTS_twt' , 'description' : '정국이 생일축하해요이?' , 'likes' : '2.9M' , 'month' : 'September' , 'year' : '2020'} 

Item23 = { 	'platform' : 'Twitter' , 'rank' : '24' , 'username' : '@BTS_twt' , 'description' : 'We met @lizzo 😍🤙' , 'likes' : '2.8M' , 'month' : 'November' , 'year' : '2021'}

Item24 = { 	'platform' : 'Twitter' , 'rank' : '25' , 'username' : '@BTS_twt' , 'description' : "It's been a long long time - bing crosby" , 'likes' : '2.8M' , 'month' : 'November' , 'year' : '2021'}

Item25 = { 	'platform' : 'Twitter' , 'rank' : '26' , 'username' : '@BTS_twt' , 'description' : '사진첩을 들어갔는데 이사진이 왜 있는지 기억이 안난다..' , 'likes' : '2.8M' , 'month' : 'September' , 'year' : '2021'}

Item26 = { 	'platform' : 'Twitter' , 'rank' : '27' , 'username' : '@BTS_twt' , 'description' : '"다녀오겠습니다😊 #JIMIN #꾸기"' , 'likes' : '2.8M' , 'month' : 'September' , 'year' : '2021'} 

Item27 = { 	'platform' : 'Twitter' , 'rank' : '28' , 'username' : '@BTS_twt' , 'description' : "It's coming. @coldplay" , 'likes' : '2.8M' , 'month' : 'September' , 'year' : '2021'}

Item28 = { 	'platform' : 'Twitter' , 'rank' : '29', 'username' : '@BTS_twt' , 'description' : '💜💜' , 'likes' : '2.8M' , 'month' : 'June' , 'year' : '2021'}

Item29 = { 	'platform' : 'Twitter' , 'rank' : '30' , 'username' : '@BTS_twt' , 'description' : '"행복했습니다♡ #JJK #SOWOOZOO"' , 'likes' : '2.8M' , 'month' : 'June' , 'year' : '2021'}

Item30 = { 	'platform' : 'Instagram' , 'rank' : '1' , 'username' : '@world_record_egg' , 'description' : 'Photo of an egg' , 'likes' : '55.9M' , 'month' : 'January' , 'year' : '2019'}

Item31 = { 	'platform' : 'Instagram' , 'rank' : '2' , 'username' : '@cristiano @georginagio' , 'description' : 'Their twins pregnancy announcement' , 'likes' : '32.8M' , 'month' : 'October' , 'year' : '2021'}

Item32 = { 	'platform' : 'Instagram' , 'rank' : '3' , 'username' : '@xxxtentacion' , 'description' : 'Final post before his death' , 'likes' : '29.1M' , 'month' : 'May' , 'year' : '2018'}

Item33 = { 	'platform' : 'Instagram' , 'rank' : '4' , 'username' : '@arianagrande' , 'description' : 'Photos from her wedding with Dalton Gomez' , 'likes' : '26.6M' , 'month' : 'May' , 'year' : '2021'}

Item34 = { 	'platform' : 'Instagram' , 'rank' : '5' , 'username' : '@kyliejenner' , 'description' : 'Second pregnancy announcement' , 'likes' : '24.9M' , 'month' : 'September' , 'year' : '2021'}

Item35 = { 'platform' : 'Instagram' , 'rank' : '6' , 'username' : '@tomholland2013' , 'description' : 'Recreating the famous Spider-Man meme with Tobey Maguire and Andrew Garfield' , 'likes' : '23.4M' , 'month' : 'February' , 'year' : '2022'}

Item36 = { 	'platform' : 'Instagram' , 'rank' : '7' , 'username' : '@kyliejenner' , 'description' : 'Photo of her daughter with her newborn brother' , 'likes' : '22.9M' , 'month' : 'February' , 'year' : '2022'}

Item37 = { 	'platform' : 'Instagram' , 'rank' : '8' , 'username' : '@billieeilish' , 'description' : 'Reveal of her blonde hair' , 'likes' : '22.9M' , 'month' : 'March' , 'year' : '2021'}

Item38 = { 	'platform' : 'Instagram' , 'rank' : '9' , 'username' : '@leomessi' , 'description' : 'First post after signing with PS' , 'likes' : '22M' , 'month' : 'August' , 'year' : '2021'}

Item39 = { 	'platform' : 'Instagram' , 'rank' : '10' , 'username' : '@billieeilish' , 'description' : 'Vogue photoshoot' , 'likes' : '21.9M' , 'month' : 'May' , 'year' : '2021'}

Item40 = { 	'platform' : 'Instagram' , 'rank' : '11' , 'username' : '@leomessi' , 'description' : 'Photo with the Copa América trophy' , 'likes' : '21.9M' , 'month' : 'July' , 'year' : '2021'}

Item41 = { 	'platform' : 'Instagram' , 'rank' : '12' , 'username' : '@leomessi' , 'description' : 'Post announcing his departure from FC Barcelona during a press conference' , 'likes' : '21.1M' , 'month' : 'August' , 'year' : '2021'}

Item42 = { 	'platform' : 'Instagram' , 'rank' : '13' , 'username' : '@tomholland2013' , 'description' : 'Happy birthday post to Zendaya' , 'likes' : '20.3M' , 'month' : 'September' , 'year' : '2021'}

Item43 = { 	'platform' : 'Instagram' , 'rank' : '14' , 'username' : '@khaby00' , 'description' : 'Reel with Brazil shirt interacting with young boy' , 'likes' : '20.2M' , 'month' : 'February' , 'year' : '2022'}

Item44 = { 	'platform' : 'Instagram' , 'rank' : '15', 'username' : '@ironshoremermaid' , 'description' : 'Interacting with young girl' , 'likes' : '20M' , 'month' : 'August' , 'year' : '2021'}

Item45 = { 	'platform' : 'Instagram' , 'rank' : '16' , 'username' : '@cristiano' , 'description' : 'Photo with his son' , 'likes' : '20M' , 'month' : 'January' , 'year' : '2022'} 

Item46 = { 	'platform' : 'Instagram' , 'rank' : '17' , 'username' : '@cristiano' , 'description' : ' Ronaldo Post in remembrance of Diego Maradona' , 'likes' : '19.7M' , 'month' : 'November' , 'year' : '2020'} 

Item47 = { 	'platform' : 'Instagram' , 'rank' : '18' , 'username' : '@thv' , 'description' : 'Photos of his dog Yeontan' , 'likes' : '19.5M' , 'month' : 'December' , 'year' : '2021'}

Item48 = { 	'platform' : 'Instagram' , 'rank' : '19' , 'username' : '@billieeilish' , 'description' : 'Arriving at the 2021 Met Gala' , 'likes' : '19.3M' , 'month' : 'September' , 'year' : '2021'}

Item49 = { 	'platform' : 'Instagram' , 'rank' : '20' , 'username' : '@cristiano' , 'description' : 'Photos of him after his second debut at Manchester United' , 'likes' : '19.3M' , 'month' : 'September' , 'year' : '2021'}

Item50 = { 	'platform' : 'Tiktok' , 'rank' : '1' , 'username' : '@bellapoarch' , 'description' : 'Lip syncing' , 'likes' : '56.5M' , 'month' : 'August' , 'year' : '2020'}

Item51 = { 	'platform' : 'Tiktok' , 'rank' : '2', 'username' : '@jamie32bsh' , 'description' : 'Dancing' , 'likes' : '51.1M' , 'month' : 'January' , 'year' : '2022'}

Item52 = { 	'platform' : 'Tiktok' , 'rank' : '3', 'username' : '@fredziownik_art' , 'description' : 'Drawing' , 'likes' : '50M' , 'month' : 'December' , 'year' : '2020'}

Item53 = { 	'platform' : 'Tiktok' , 'rank' : '4' , 'username' : '@thenickluciano' , 'description' : 'Lip syncing' , 'likes' : '48.5M' , 'month' : 'February' , 'year' : '2021'}

Item54 = { 	'platform' : 'Tiktok' , 'rank' : '5' , 'username' : '@totouchanemu' , 'description' : 'Dancing' , 'likes' : '44.4M' , 'month' : 'July' , 'year' : '2021'}

Item55 = { 	'platform' : 'Tiktok' , 'rank' : '6' , 'username' : '@adrianchateau' , 'description' : 'Comedy' , 'likes' : '40.1M' , 'month' : 'November' , 'year' : '2021'}

Item56 = { 	'platform' : 'Tiktok' , 'rank' : '7' , 'username' : ' 	@billieeilish' , 'description' : 'Time Warp Scan" filter' , 'likes' : '39.9M' , 'month' : 'November' , 'year' : '2022'}

Item57 = { 	'platform' : 'Tiktok' , 'rank' : '8' , 'username' : ' 	@mngnzls' , 'description' : 'Sang “Suave - El Alfa” originally' , 'likes' : '39.1M' , 'month' : 'March' , 'year' : '2022'}

Item58 = { 	'platform' : 'Tiktok' , 'rank' : '9' , 'username' : '@khaby.lame' , 'description' : 'Peeling a banana' , 'likes' : '37.8M' , 'month' : 'April' , 'year' : '2021'}

Item59 = { 	'platform' : 'Tiktok' , 'rank' : '10' , 'username' : ' 	@britishpromise.cats' , 'description' : 'Cat pawing at camera' , 'likes' : '36.7M' , 'month' : 'June' , 'year' : '2020' }

Item60 = { 	'platform' : 'Tiktok' , 'rank' : '11' , 'username' : '@khaby.lame' , 'description' : ' 	Opening a car door' , 'likes' : '36.1M' , 'month' : 'June ' , 'year' : '2021'}

Item61 = { 	'platform' : 'Tiktok' , 'rank' : '12' , 'username' : '@khaby.lame' , 'description' : 'Opening a door' , 'likes' : '35.4M' , 'month' : 'June' , 'year' : '2021'}

Item62 = { 	'platform' : 'Tiktok' , 'rank' : '13' , 'username' : '@chipmunksoftiktok' , 'description' : "A chipmunk eating nuts out of someone's hand" , 'likes' : '35.2M' , 'month' : 'June' , 'year' : '2021'}

Item63 = { 	'platform' : 'Tiktok' , 'rank' : '14' , 'username' : '@daexo' , 'description' : ' 	Baby' , 'likes' : '34.9M' , 'month' : 'September' , 'year' : '2021'}

Item64 = { 	'platform' : 'Tiktok' , 'rank' : '15' , 'username' : '@enbiggen' , 'description' : 'Spirited Away animation' , 'likes' : '34.9M' , 'month' : 'September' , 'year' : '2021' }

Item65 = { 	'platform' : 'Tiktok' , 'rank' : '16' , 'username' : '@khaby.lame' , 'description' : 'Removing mask from cup handle' , 'likes' : '34.6M' , 'month' : 'April' , 'year' : '2021' }

Item66 = { 	'platform' : 'Tiktok' , 'rank' : '17' , 'username' : '@cikiee' , 'description' : ' 	Pick-up line' , 'likes' : '33.3M' , 'month' : 'June' , 'year' : '2021'}

Item67 = { 	'platform' : 'Tiktok' , 'rank' : '18' , 'username' : '@derik.munson' , 'description' : 'Penguin tipped the iceberg itself' , 'likes' : '33.1M' , 'month' : 'January' , 'year' : '2022' }

Item68 = { 	'platform' : 'Tiktok' , 'rank' : '19' , 'username' : '@khaby.lame' , 'description' : 'Drinking a glass of water' , 'likes' : '32.3M' , 'month' : 'April' , 'year' : '2021' }

Item69 = { 	'platform' : 'Tiktok' , 'rank' : '20' , 'username' : '@ninachristine15' , 'description' : 'Kitten running' , 'likes' : '32.2M' , 'month' : 'January' , 'year' : '2021' }

Item70 = { 	'platform' : 'Tiktok' , 'rank' : '21' , 'username' : '@cacha.7.griselda' , 'description' : 'Dancing' , 'likes' : '31.5M' , 'month' : 'July' , 'year' : '2021' }

Item71 = { 	'platform' : 'Tiktok' , 'rank' : '22' , 'username' : '@khaby.lame' , 'description' : 'Removing stuck t-shirt from car door' , 'likes' : '30.8M' , 'month' : 'May' , 'year' : '2021' }

Item72 = { 	'platform' : 'Tiktok' , 'rank' : '23' , 'username' : '@my_aussie_gal' , 'description' : 'Dog painting a flower' , 'likes' : '30.8M' , 'month' : 'July' , 'year' : '2021' }

Item73 = { 	'platform' : 'Tiktok' , 'rank' : '24' , 'username' : '@fxxkmin17' , 'description' : 'Lioness hugging her owner' , 'likes' : '30.4M' , 'month' : 'February' , 'year' : '2021' }

Item74 = { 	'platform' : 'Tiktok' , 'rank' : '25' , 'username' : '@igor.molodtsov' , 'description' : 'Designing an airpods wireless generation case' , 'likes' : '30.4M' , 'month' : 'April' , 'year' : '2021' }

Item75 = { 	'platform' : 'Tiktok' , 'rank' : '26' , 'username' : '@kikakiim' , 'description' : 'Light-up on the cupcake wishing happy birthday to herself' , 'likes' : '30.3M' , 'month' : 'July' , 'year' : '2021' }

Item76 = { 	'platform' : 'YouTube' , 'rank' : '1' , 'username' : 'Luis Fonsi featuring Daddy Yankee' , 'description' : 'Despacito' , 'likes' : '48.16M' , 'month' : 'January' , 'year' : '2017' }

Item77 = { 	'platform' : 'YouTube' , 'rank' : '2' , 'username' : 'Wiz Khalifa featuring Charlie Puth' , 'description' : 'See You Again' , 'likes' : '37.73M' , 'month' : 'April' , 'year' : '2015' }

Item78 = { 	'platform' : 'YouTube' , 'rank' : '3' , 'username' : "Pinkfong Kids' Songs & Stories", 'description' : 'Baby Shark Dance' , 'likes' : '34.6M' , 'month' : 'June' , 'year' : '2016' }

Item79 = { 	'platform' : 'YouTube' , 'rank' : '4' , 'username' : 'BTS' , 'description' : 'Dynamite' , 'likes' : '33.58M' , 'month' : 'August' , 'year' : '2020'}

Item80 = { 	'platform' : 'YouTube' , 'rank' : '5' , 'username' : 'Ed Sheeran' , 'description' : 'Shape of You' , 'likes' : '29.53M' , 'month' : 'January' , 'year' : '2017' }

Item81 = { 	'platform' : 'YouTube' , 'rank' : '6' , 'username' : 'BTS featuring Halsey' , 'description' : 'Boy with Luv' , 'likes' : '26.03M' , 'month' : 'April' , 'year' : '2019' }

Item82 = { 	'platform' : 'YouTube' , 'rank' : '7' , 'username' : 'Alan Walker' , 'description' : 'Faded' , 'likes' : '25.12M' , 'month' : 'December' , 'year' : '2015' }

Item83 = { 	'platform' : 'YouTube' , 'rank' : '8' , 'username' : 'Psy' , 'description' : 'Gangnam Style' , 'likes' : '24.23M' , 'month' : 'July' , 'year' : '2012' }

Item84 = { 	'platform' : 'YouTube' , 'rank' : '9' , 'username' : 'Zach King' , 'description' : 'How Zach King Gets Away With Doing Graffiti' , 'likes' : '24M' , 'month' : 'July' , 'year' : '2019'}

Item85 = { 	'platform' : 'YouTube' , 'rank' : '10' , 'username' : 'Blackpink' , 'description' : 'How You Like That' , 'likes' : '23.23M' , 'month' : 'June' , 'year' : '2020'}

Item86 = { 	'platform' : 'YouTube' , 'rank' : '11' , 'username' : 'Marshmello' , 'description' : 'Alone' , 'likes' : '23.04M' , 'month' : 'July' , 'year' : '2016'}

Item87 = { 	'platform' : 'YouTube' , 'rank' : '12' , 'username' : 'Blackpink' , 'description' : 'Kill This Love' , 'likes' : '22.44M' , 'month' : 'April' , 'year' : '2019'}

Item88 = { 	'platform' : 'YouTube' , 'rank' : '13' , 'username' : 'Billie Eilish and Khalid' , 'description' : 'Lovely' , 'likes' : '22.08M' , 'month' : 'April' , 'year' : '2018' }

Item89 = { 	'platform' : 'YouTube' , 'rank' : '14' , 'username' : 'BTS' , 'description' : 'Butter' , 'likes' : '21.72M' , 'month' : 'May' , 'year' : '2021' }

Item90 = { 	'platform' : 'YouTube' , 'rank' : '15' , 'username' : 'BTS' , 'description' : 'DNA' , 'likes' : '21.67M' , 'month' : 'September' , 'year' : '2017' }

Item91 = { 	'platform' : 'YouTube' , 'rank' : '16' , 'username' : 'Justin Bieber featuring Ludacris' , 'description' : 'Baby' , 'likes' : '21.05M' , 'month' : 'February' , 'year' : '2010' }

Item92 = { 	'platform' : 'YouTube' , 'rank' : '17' , 'username' : 'Blackpink' , 'description' : 'Ddu-Du Ddu-Du' , 'likes' : '20.89M' , 'month' : 'June' , 'year' : '2018'}

Item93 = { 	'platform' : 'YouTube' , 'rank' : '18' , 'username' : 'Maroon 5 featuring Cardi B' , 'description' : 'Girls Like You' , 'likes' : '20.28M' , 'month' : 'May' , 'year' : '2018'}

Item94 = { 	'platform' : 'YouTube' , 'rank' : '19' , 'username' : 'MrBeast' , 'description' : 'Make This Video The Most Liked Video On Youtube' , 'likes' : '19.5M' , 'month' : 'January' , 'year' : '2019'}

Item95 = { 	'platform' : 'YouTube' , 'rank' : '20' , 'username' : 'BTS' , 'description' : 'Fake Love' , 'likes' : '19.4M' , 'month' : 'May	 ' , 'year' : '2018'}

Item96 = { 	'platform' : 'YouTube' , 'rank' : '21' , 'username' : 'Imagine Dragons' , 'description' : 'Believer' , 'likes' : '19.2M' , 'month' : 'March' , 'year' : '2017'}

Item97 = { 	'platform' : 'YouTube' , 'rank' : '22' , 'username' : 'BTS' , 'description' : 'Idol' , 'likes' : '19.18M' , 'month' : 'August' , 'year' : '2018'}

Item98 = { 	'platform' : 'YouTube' , 'rank' : '23' , 'username' : 'Shawn Mendes and Camila Cabello' , 'description' : 'Señorita' , 'likes' : '18.93M' , 'month' : 'June' , 'year' : '2019' }

Item99 = { 	'platform' : 'YouTube' , 'rank' : '24' , 'username' : 'Mark Ronson featuring Bruno Mars' , 'description' : 'Uptown Funk' , 'likes' : '18.67M' , 'month' : 'November' , 'year' : '2014'}

Item100 = { 'platform' : 'YouTube' , 'rank' : '25' , 'username' : 'Blackpink and Selena Gomez' , 'description' : 'Ice Cream' , 'likes' : '18.51M' , 'month' : 'August' , 'year' : '2020' }

Item101 = { 'platform' : 'YouTube' , 'rank' : '26' , 'username' : 'BTS' , 'description' : 'Mic Drop' , 'likes' : '18.25M' , 'month' : 'November' , 'year' : '2017' }

Item102 = { 'platform' : 'YouTube' , 'rank' : '27' , 'username' : 'Adele' , 'description' : 'Hello' , 'likes' : '17.73M' , 'month' : 'October' , 'year' : '2015' }

Item103 = { 'platform' : 'YouTube' , 'rank' : '28' , 'username' : 'DJ Snake featuring Selena Gomez, Ozuna & Cardi B' , 'description' : 'Taki Taki' , 'likes' : '17.7M' , 'month' : 'October' , 'year' : '2018'}

Item104 = { 'platform' : 'YouTube' , 'rank' : '29' , 'username' : 'Eminem' , 'description' : 'Rap God' , 'likes' : '17.55M' , 'month' : 'November' , 'year' : '2013' }

Item105 = { 'platform' : 'YouTube' , 'rank' : '30' , 'username' : 'Billie Eilish' , 'description' : 'Bad Guy' , 'likes' : '17.32M' , 'month' : 'March' , 'year' : '2019'} 

Item106 = { 'platform' : 'Twitter' , 'rank' : '31' , 'username' : '@BarackObama' , 'description' : "Thank you for everything. My last ask is the same as my first. I'm asking you to believe—not in my ability to create change, but in yours." , 'likes' : '2.6M' , 'month' : 'January' , 'year' : '2017'}

Item107 = { 'platform' : 'Twitter' , 'rank' : '32' , 'username' : '@BarackObama' , 'description' : "It's been the honor of my life to serve you. You made me a better man." , 'likes' : '2.4M' , 'month' : 'January' , 'year' : '2017'}

Item108 = { 'platform' : 'Instagram' , 'rank' : '21' , 'username' : '@kyliejenner' , 'description' : 'Kylie introduces her baby girl, Stormi' , 'likes' : '18M' , 'month' : 'February' , 'year' : '2018'}

Item109 = { 'platform' : 'Instagram' , 'rank' : '22' , 'username' : '@justinbieber' , 'description' : 'Justin Bieber confirms his engagement to Hailey Baldwin' , 'likes' : '13.3M' , 'month' : 'July' , 'year' : '2018'}

Item110 = { 'platform' : 'Instagram' , 'rank' : '23' , 'username' : '@kyliejenner' , 'description' : 'Kylie and Stormi' , 'likes' : '13M' , 'month' : 'March' , 'year' : '2018'}

Item111 = { 'platform' : 'Instagram' , 'rank' : '24' , 'username' : '@arianagrande' , 'description' : "Ariana Grande's tribute for Mac Miller" , 'likes' : '12.8M' , 'month' : 'September' , 'year' : '2018'}

Item112 = { 'platform' : 'Instagram' , 'rank' : '25' , 'username' : '@cristiano' , 'description' : 'Cristiano Ronaldo confirms he is joining Juventus' , 'likes' : '12.2M' , 'month' : 'July' , 'year' : '2018'}

Item113 = { 'platform' : 'Instagram' , 'rank' : '26' , 'username' : '@kyliejenner' , 'description' : 'Kylie and Stormi, but this time for Halloween' , 'likes' : '11.8M' , 'month' : 'October' , 'year' : '2018'}

Item114 = { 'platform' : 'Instagram' , 'rank' : '27' , 'username' : '@cristiano' , 'description' : "Cristiano Ronaldo's date night snap" , 'likes' : '11.3M' , 'month' : 'July' , 'year' : '2018'}

Item115 = { 'platform' : 'Instagram' , 'rank' : '28' , 'username' : '@cristiano' , 'description' : 'Ronaldo and his family in the hospital for the birth of his daughter' , 'likes' : '11.1M' , 'month' : 'November' , 'year' : '2017'}

Item116 = { 'platform' : 'Instagram' , 'rank' : '29' , 'username' : '@beyonce' , 'description' : "Beyoncé's pregnancy announcement" , 'likes' : '10.9M' , 'month' : 'February' , 'year' : '2017'}

Item117 = { 'platform' : 'Instagram' , 'rank' : '30' , 'username' : '@selenagomez' , 'description' : ' An announcement from Gomez that detailed her health issues and recent kidney transplant' , 'likes' : '10.5M' , 'month' : 'September' , 'year' : '2017'}

Item118 = { 'platform' : 'Instagram' , 'rank' : '31' , 'username' : '@beyonce' , 'description' : 'Beyoncé and her newborn twins' , 'likes' : '10M' , 'month' : 'July' , 'year' : '2017'}

Item119 = { 'platform' : 'Instagram' , 'rank' : '32' , 'username' : '@cristiano' , 'description' : 'Ronaldo and his newborn twins' , 'likes' : '7.9M' , 'month' : 'June' , 'year' : '2017'}

Item120 = { 'platform' : 'Tiktok' , 'rank' : '27' , 'username' : '@bellapoarch' , 'description' : 'Doing an Archery trick' , 'likes' : '29.3M' , 'month' : 'March' , 'year' : '2022'}

    #inserted items here 
# db.insert(Item00)
# db.insert(Item01)
# db.insert(Item02)
# db.insert(Item03)
# db.insert(Item04)
# db.insert(Item05)
# db.insert(Item06)
# db.insert(Item07)
# db.insert(Item08)
# db.insert(Item09)
# db.insert(Item10)
# db.insert(Item11)
# db.insert(Item12)
# db.insert(Item13)
# db.insert(Item14)
# db.insert(Item15)
# db.insert(Item16)
# db.insert(Item17)
# db.insert(Item18)
# db.insert(Item19)
# db.insert(Item20)
# db.insert(Item21)
# db.insert(Item22)
# db.insert(Item23)
# db.insert(Item24)
# db.insert(Item25)
# db.insert(Item26)
# db.insert(Item27)
# db.insert(Item28)
# db.insert(Item29)
# db.insert(Item30)
# db.insert(Item31)
# db.insert(Item32)
# db.insert(Item33)
# db.insert(Item34)
# db.insert(Item35)
# db.insert(Item36)
# db.insert(Item37)
# db.insert(Item38)
# db.insert(Item39)
# db.insert(Item40)
# db.insert(Item41)
# db.insert(Item42)
# db.insert(Item43)
# db.insert(Item44)
# db.insert(Item45)
# db.insert(Item46)
# db.insert(Item47)
# db.insert(Item48)
# db.insert(Item49)
# db.insert(Item50)
# db.insert(Item51)
# db.insert(Item52)
# db.insert(Item53)
# db.insert(Item54)
# db.insert(Item55)
# db.insert(Item56)
# db.insert(Item57)
# db.insert(Item58)
# db.insert(Item59)
# db.insert(Item60)
# db.insert(Item61)
# db.insert(Item62)
# db.insert(Item63)
# db.insert(Item64)
# db.insert(Item65)
# db.insert(Item66)
# db.insert(Item67)
# db.insert(Item68)
# db.insert(Item69)
# db.insert(Item70)
# db.insert(Item71)
# db.insert(Item72)
# db.insert(Item73)
# db.insert(Item74)
# db.insert(Item75)
# db.insert(Item76)
# db.insert(Item77)
# db.insert(Item78)
# db.insert(Item79)
# db.insert(Item80)
# db.insert(Item81)
# db.insert(Item82)
# db.insert(Item83)
# db.insert(Item84)
# db.insert(Item85)
# db.insert(Item86)
# db.insert(Item87)
# db.insert(Item88)
# db.insert(Item89)
# db.insert(Item90)
# db.insert(Item91)
# db.insert(Item92)
# db.insert(Item93)
# db.insert(Item94)
# db.insert(Item95)
# db.insert(Item96)
# db.insert(Item97)
# db.insert(Item98)
# db.insert(Item99)
# db.insert(Item100)
# db.insert(Item101)
# db.insert(Item102)
# db.insert(Item103)
# db.insert(Item104)
# db.insert(Item105)
# db.insert(Item106)
# db.insert(Item107)
# db.insert(Item108)
# db.insert(Item109)
# db.insert(Item110)
# db.insert(Item111)
# db.insert(Item112)
# db.insert(Item113)
# db.insert(Item114)
# db.insert(Item115)
# db.insert(Item116)
# db.insert(Item117)
# db.insert(Item118)
# db.insert(Item119)
# db.insert(Item120)

#DATABASE FUNCTIONS 
    #search a specific platform for a specific year
def search_for_platform_year(platform, year):
    result = db.search((Info.platform == platform) & (Info.year == year))
    return result 

    #search a specific rank for a specific platform
def search_for_platfrom_rank(platform, rank):
    result = db.search((Info.platform == platform) & (Info.rank == rank))
    return result 

    #Give a rank and get the result of that rank for all platforms
def all_platforms_rank(rank): 
    result = db.search(Info.rank == rank) 
    return result

    #look for all post from a specific platform 
def all_posts_from_one_platform(platform): 
    result = db.search(Info.platform == platform) 
    return result

    #searched for a certain year across all platforms
def one_year_all_platforms(year):
    result = db.search(Info.year == year) 
    return result

    #for each media it shows how many tweets per user 
def tweets_per_user():
    result = db.search(Info.username == Info.username) #just prints the whole database 
    return result 

#USER INTERFACE 
def user_interface():
    #print choice menu to user 
    print("\n---------------------CS432 Project3---------------------")
    print("Description: Analyziing social media data. We used four social media platfroms with. Data is sorted by rank.")
    print("Data Available:   ")
    print("     Platforms: Twitter, Instragram, Tiktok, Youtube")
    print("     Ranks for each: Twitter(1-32), Intragram(1-32), Tiktok(1-27), Youtube(1-30)")
    print("     Years for each: Twitter(2017-2022), Instagram(2018-2022), Tiktok(2020-2022), Youtube(2010-2021)\n")
    print("Options: ")
    print("[0] Exit ")
    print("[1] Search a specific platform for a specific year")
    print("[2] Search a specific rank for a specific platform")
    print("[3] Give a rank and get the result of that rank for all platforms")
    print("[4] Look for all post from a specific platform")
    print("[5] Searched for a certain year across all platforms")
    print("[6] for each media it shows how many posts per user\n") #working on 

    #take in user input 
    option = int(input("Enter an option: "))

    while option != 0:
        if option == 1:
            platform = input("Enter platform name: ")
            year = input("Enter year: ")
            #perform op
            #print result 
            print(search_for_platform_year(platform, year))
            print("\n")

        elif option == 2:
            platform1 = input("Enter platform: ")
            rank1 = input("Enter rank: ")
            #perform op
            #print result 
            print(search_for_platfrom_rank(platform1, rank1))
            print("\n")

        elif option == 3:
            rank2 = input("Enter rank: ")
            #perform op
            #print result 
            print(all_platforms_rank(rank2))
            print("\n")
        
        elif option == 4:
            #perform op
            #print result 
            platform2 = input("Enter platform: ")
            print(all_posts_from_one_platform(platform2))
            print("\n")

        elif option == 5:
            #perform op
            #print result 
            year1 = input("Enter year: ")
            print(one_year_all_platforms(year1))
            print("\n")

        elif option == 6:
            #perform op
            #print result 
            print(tweets_per_user())
            print("\n")

        else:
            #option to exit program
            option = 0
            print("invalid choice!")
        
        #loop (retake user input until program is exited)
        option = int(input("Enter an option: "))
    
    #exit message 
    print("Program exited")

#run user interface 
user_interface()
