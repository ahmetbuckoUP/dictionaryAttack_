# dictionaryAttack_
Ne kete ushtrim ne kemi kryer nje sulm me sqlDict tool ne Kali linux, dhe kemi krijuar nje Dictionary Attack concole application ne Python.

![image](https://user-images.githubusercontent.com/75639075/102727299-2f384580-4325-11eb-84dc-d21caa74ce8c.png)

Ku ne IP: jepet target server, jepet account username dhe bohet load nje file.txt me passworda ku aplikacioni fillon ta sulmoj aplikacioni.

![image](https://user-images.githubusercontent.com/75639075/102829724-0462f580-43e8-11eb-981e-31d5357d07d7.png)

Por pasi msqldict eshte nje softuer shume i vjeter dhe me serverat e ri per shkaqe te sigurise nuk kthejne response nese bejne kerkese ne server. Ne si grup jemi munduar qe te krijojme nje program qe kryen dictionary attack sulme, funksionin e njejte qe kryen edhe msqldict.
Aplikacioni jone eshte shkruar ne gjuhen python, dhe perdor librarine scrapy per te lidhur me serverin dhe per te bere dictionary attack ne serverin e paracaktuar.

![image](https://user-images.githubusercontent.com/75639075/102830079-d631e580-43e8-11eb-9ad3-06858abe11b3.png)

skripta lexon nga file pass.txt dhe merr secilen password per ta provuar, .txt file na doket keshtu.

![image](https://user-images.githubusercontent.com/75639075/102830182-09747480-43e9-11eb-8b4e-839b950cc580.png)


Dhe pasi qe ta startojme skripten duke targetuar login e faqes, ku njeherit e njejta kerkon nje username dhe lexon .txt file dhe dergon requesta ne server deri sa te arrihet logini.
p.s. me te verdha jane te paraqitur username dhe kur breach ka ndodhur pra useri eshte qasur ne kontent.

![image](https://user-images.githubusercontent.com/75639075/102830271-43de1180-43e9-11eb-84b2-284d7f6f5fd5.png)

Punuar nga: Ahmet Bucko, Albion Berisha dhe Ardian Reçiça.
