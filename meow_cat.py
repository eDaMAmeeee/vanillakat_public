"""
「そのまま使えるVanillaKat！」
ご自由にお使いください。(使う際は一言連絡あると嬉しい)

Created by 莉於#6196 (2019-2021).
Discord : discord.gg/PvpTarv

必須ライブラリ：discord,random,datetime

だいぶ初期に作ったのでボロボロです。
"""

import discord,random
from datetime import datetime

time=datetime.now()
hour=time.h
min=time.minute

client=discord.Client()
discord_token="xxx" #ここ変えるだけ

@client.event
async def on_message(message)

#特別(sou7さんのGreeting bot用)
    if message.author.id == 394876010438328321:
        if message.content == "はにゃー！":
            c=["はにゃーじゃねえよ！","は..はにゃー","...","ジー...は..にゃー..","は..はにゃー？","は..はぁ..にゃあ？","^^#"]
            choice=random.choice(c)
            await message.channel.send(choice)
        elif message.content.startswith("かわいいにゃ"):
            c=["え...","^^#","そ..そお？","ジー（冷めた目）","そうでもないこともないにゃ","う..うん"]
            choice=random.choice(c)
            await message.channel.send(choice)
        elif message.content == "なー":
            c=["なー..","う..うん","にー","^^#","あ！UFOだ！","え..."]
            choice=random.choice(c)
            await message.channel.send(choice)
        elif message.content == "にゃぁ～....ってあっ！":
            c=["い！","ん？","^^#","ん？あ！UFOだ！","にゃ～"]
            choice=random.choice(c)
            await message.channel.send(choice)
        else:
            return
            
#挨拶
    if message.content.endswith("だよね？"):
        await message.channel.send("そうだな")
    elif "絶対" in message.content and "だな" in message.content:
        await message.channel.send("俺もそう思う")
    elif message.content == "だる":
        c=["そうだな","俺はそう思わない","クエー","やっぱり狂ってるね","耐水耐圧耐衝撃スマホでも15万やぞ","確かに1年間は無防備ではあるが…","あは"]
        msg=random.choice(c)
        await message.channel.send(msg)
    elif message.content == "なー":
        await message.channel.send("ねー")
    elif message.content == "同意して":
        await message.channel.send("私もそう思います")
    elif message.content == "いい夢みろよ":
        c=["おう！","ういいす！","はーい","うむ","ほい","クエー","ぐわははは","ふむ","ぽむ！","もふ！","ふぉわ！"]
        choice=random.choice(c)
        await message.channel.send(choice)
    elif message.content == "偽物のポケモン作って" or message.content == "偽物のpokemon作って":
        embed=discord.Embed(title="A wild pokémon has appeared!",description="Guess the pokémon and type p!catch <pokémon> to catch it!",color=0x00ae86)
        embed.set_image(url=message.author.avatar_url_as(format="png"))
        await message.channel.send(embed=embed)
    elif message.content == "hey siri":
        c=["呼んだかな?おっと私はムスカ大佐だった","Siriなど眼中にないわぁ","フハハハ","お呼びでしょうか","くええええ"]
        msg=random.choice(c)
        await message.channel.send(msg)
    elif "信じてる？" in message.content or "信じる？" in message.content:
        await message.channel.send("信じるか信じないかは、あなた次第です")
        return
    elif message.content.startswith("フハハハ"):
        c=["フハハハハ。それは残像だ！","メロンパンをよこせー","むむ！","グハ！まさか勇者だと！","どした？","ふぇええ","クエー","ま、、まさか、、","デフ！","Error:`チョットナニイッテルカワカリマセンデシタ`"]
        choice=random.choice(c)
        await message.channel.send(choice)
    elif message.content == "うるさい":
        await message.channel.send("言葉をつつしみたまえ！！君はおこちゃま大魔王の前にいるのだ！！")
    elif message.content == "読めない":
        await message.channel.send("読める！！読めるぞ！！")
    elif message.content == "どうしよう":
        await message.channel.send("お前達はここで待て！")
    elif message.content == "終わった":
        await message.channel.send("いえ、これからです")
    elif message.content == "やっと終わった":
        await message.channel.send("だがやつは四天王の中でも最弱...")
    elif "夜行性" in message.content and "許して" in message.content:
        c=["なるほど","じゃあ許すわ","フム","クエー","許す","ほお"]
        choice=random.choice(c)
        await message.channel.send(choice)
    elif message.content == "おちる":
        c=["お疲れぃ！","クエー","今日の働き誠に大義であった。褒美を授けよう","お疲れ～","ぐえええええええええええええ","くゑー"]
        choice=random.choice(c)
        await message.channel.send(choice)
    elif message.content == "て　す　と":
        c=["な ん の","クエー","テスト中","ふむ","うむ"]
        await message.channel.send(random.choice(c))
    elif message.content.startswith("我こそは大いなるお子ちゃま大魔王様"):
        c=["クエ！？","出たな偽物め！","なに！","クエー","！","ムム！","なんだと！","フハハハハ！それは残像さ！","クエ・・"]
        choice=random.choice(c)
        await message.channel.send("{}我こそが本当の大いなるお子ちゃま大魔王様であるぞ！".format(choice))
    elif message.content == "さようなら":
        await message.channel.send("さようなら")
    elif "ダメージを受けた" in message.content:
        await message.channel.send("グハ！お主、なかなかやるな。ただものではないな！何者だ！まさか勇者だと！")
    elif "誰もいない" in message.content:
        await message.channel.send("ねえそういえば話変わるけど誰もいないといえばクラスの女子から「今家に誰もいないから来て」って言われていったらその女子もいなかった")
        return
    elif "留守番" in message.content:
        await message.channel.send("ねえそういえばさぁ。話変わるけどこの前留守番と言えば一人息子がちゃんと留守番できているかどうか、公衆電話から他人のふりをして家に電話してみた。")
        await message.channel.send("俺「もしもし、お母さんいる？」\n息子「いらない」\nって言われた")
        return
    elif message.content == "詐欺":
        await message.channel.send("あ。そういえば話変わるけど詐欺と言えば昨日うちのじーちゃんが「詐欺商法にだまされない本」という本を３０万円で買ってきた")
        return
    elif "ボケ防止" in message.content:
        await message.channel.send("ねえ、話変わるけどボケと言えば、昨日じいちゃんが「ボケないための本」を買ってきた\n今日も買ってきた")
        return
    elif "マック" in message.content:
        if message.author.bot:
            return
        msg="""
            話変わるけどマックと言えば今日友人とマックに行った。
        そしたら隣のカップルが喧嘩し始めて、ついに彼女が帰ってしまった。
        ひとり残される彼氏。
        彼は「なんだよ・・・」とつぶやきながら、くわえていたポテトに火をつけようとしていた"""
        await message.channel.send(msg)
        return
    elif "バス停" in message.content:
        if message.author.bot:
            return
        await message.channel.send("話変わるけどバス停と言えばかつて、バス停を毎日ちょっとずつ家の方に近づけていた。")
        await message.channel.send("苦労して毎日コツコツとやったのに、ある日一気に元の位置に戻された。 \nふざけんな。")
        return
    elif "チキン" in message.content:
        if message.author.bot:
            return
        await message.channel.send("話変わるけどチキンと言えばミニストップでファーストフード頼んだ時に\n「骨なしチキンのお客様ー！」って呼び出されたんだけど、、、")
        await message.channel.send("なんかすごい罵詈雑言を浴びせられたような気がする")
        return
    elif message.content == "通信速度": #pingおまけです
        t1 = message.created_at
        m = await message.channel.send('クエー')
        time = (m.created_at - t1).total_seconds() * 1000
        await m.edit(content='`{}ms`です'.format(int(time)))
    elif message.content == "pikoki-は黙れ":
        await message.channel.send("言っても僕は黙らないぞ！")
    elif "魔女" in message.content:
        await message.channel.send("キキ「あの、私、魔女のキキです。こっちはレディのガガ。」")
        return
    elif "きよしこの夜" in message.content:
        await message.channel.send("「きよしこの夜」のきよしこって誰？")
        return
    elif message.content == "スネ夫の名言":
        c=["悪いなのび太、このゲームは3人までなんだ","先生！生徒に暴力をふるってはいけません！","美しいということばは、ぼくのためにあるんだなあ。"]
        choice=random.choice(c)
        embed=discord.Embed(title=choice,description=(),color=discord.Color(random.randint(0,0xFFFFFF)))
        embed.set_author(name="骨川スネ夫",icon_url="https://pbs.twimg.com/profile_images/681367744416059392/f9eja41S_400x400.jpg")
        await message.channel.send(embed=embed)
    elif message.content == "ジャイアンの名言":
        c=["お前のものは俺のもの。俺のものも俺のもの","正しいのはいつもおれだ","永久に借りておくだけだぞ","心の友よ！"]
        choice=random.choice(c)
        embed=discord.Embed(title=choice,description=(),color=discord.Color(random.randint(0,0xFFFFFF)))
        embed.set_author(name="剛田武",icon_url="http://makisimamu.xyz/wp-content/uploads/2017/01/aa-109.png")
        await message.channel.send(embed=embed)
    # elif message.content == "ウイルスかかった": #このご時世ちょっとやめとこ。
        # await message.channel.send("あなたがかかったのはAのウイルスですか？それともBのウイルスですか？\n正直なあなたには両方あげましょう")
    elif message.content == "熱盛":
        c=["<:atsumori:584609302199795723>","失礼しました。熱盛と出てしまいました。"] #熱盛の絵文字、各自でご用意ください。
        choice=random.choice(c)
        await message.channel.send(choice)
    elif "余裕" in message.content:
        c=["メロンパンをよこせーーー","背負い投げ～","なに！まさかプロか！","激安！","一本！","よ..余裕だと...!"]
        await message.channel.send(random.choice(c))
        return
    elif message.content == "見て":
        await message.channel.send("まさか見ると視界が壊れるやつか")
    elif message.content == "無理":
        await message.channel.send("少年よ大志を抱け")
    elif "必殺技" in message.content:
        await message.channel.send("くらえー　　　メラ")
        return
    elif message.content == "起きた" or message.content == "起きたよ":
        c=["よく眠れたかな？","おはよ","おはよう","おはようでござる","おはようございます","クエー","モー","( ノﾟДﾟ)おはよう","~~~ヾ(＾∇＾)おはよー♪"]
        choice=random.choice(c)
        await message.channel.send(choice)
    elif "捕獲" in message.content:
        if message.author.bot:
            return
        await message.channel.send("そんなバカな\n僕が捕獲されるじゃと")
        return
    elif "司法解剖" in message.content:
        if message.author.bot:
            return
        await message.channel.send("司法解剖の結果、死因は司法解剖であった。")
        return
    if message.content.startswith("ふはは"):
        if message.author.bot:
            return
        await message.channel.send("フハハハハ　それは残像だ")
    if message.content == "ガード！":
        if message.author.bot:
            return
        await message.channel.send("俺のファイアボールをふせぐだと")
    elif "いじめ" in message.content and "靴" in message.content:
        if message.author.bot:
            return
        await message.channel.send("ゴミ箱から俺の靴が\nクラス会議勃発\n先生に慰められる俺\n新しいの買ったから自分で捨てたなんて言えない空気")
        return
    elif message.content == "駐車場":
        await message.channel.send("駐車場と言えばだいぶ前に某飲食店の「お客様の声」に、駐車場を増やして欲しいです、と書いておいた。")
        await message.channel.send("後日その店を訪れると、店のあった場所に広い駐車場ができていた。")
    elif message.content == "チャンネルトピックは？":
        await message.channel.send("```{}```".format(message.channel.topic))
    elif message.content == "LOL":
        await message.channel.send("🇱 🇴 🇱")
    elif message.content == "デブ":
        await message.channel.send("デブ「俺が太ってるんじゃない。太ってるのが俺なんだ」")
    elif message.content == "ホームステイ":
        await message.channel.send("俺「卒業後5年間ほどホームステイを」\n面接官「ちなみにどちらへ？」\n俺「自宅です」")
    elif message.content == "ギャンブル":
        await message.channel.send("ギャンブルと言えば友達が「俺はもう絶対にギャンブルなんかしねぇんだ。賭けてもいいぜ！！」って言ってた")
    elif message.content == "新幹線":
        await message.channel.send("新幹線と言えば、新幹線に��めて乗った時、座席を倒そうと手元のボタンを押したら隣のおっさんが倒れていった")
    elif message.content == "インド":
        await message.channel.send("「インドの人って右手でごはん食べるんだって」\n「えっ！口じゃねーんだ！！」")
    elif message.content == "まさか！":
        await message.channel.send("フハハハハ  地獄の底から這い上がって来たぞ")
    elif message.content == "よろしくおねがいします" or message.content == "よろしくお願いします":
        c=["ボンジュールでごわす","お！イケメン！","ドモドモ","お前はまさかあの時の村長か","よろしくクエー","クエー","その出会いがあなたの人生にどんな影響をもたらすのか。それは誰にも分かりません。"]
        c1=["世界に平和を！","窒素ってどんな味？","３文字で自己紹介をﾄﾞｰｿﾞ","私はバニラ大佐だ","その出会いがあなたの人生にどんな影響をもたらすのか。それは誰にも分かりません。","クエクエ"]
        c2=random.choice(c)
        c3=random.choice(c1)
        l=[c2,c3]
        msg=random.choice(l)
        await message.channel.send(msg)
    if message.content.startswith("うわ"):
        c=["さぁゲームを始めようか","お前があのときの村長だったのか！","村長、ゾンビが攻めてきています","ダイエットしたいけどメロンパン食いてぇ"]
        msg=random.choice(c)
        await message.channel.send(msg)
    if message.content == "ない":
        await message.channel.send("さがせ！この世のすべてをそこにおいてきた！")
    if message.content == "RIP":
        await message.channel.send("そのまま永遠に眠るがよい")
    elif "くらえ" in message.content:
        await message.channel.send("クエーーー目がーー")
        return
    elif "巨人" in message.content:
        await message.channel.send("巨人を食い尽くしてやる！！")
        return
    elif message.content == "カレー":
        await message.channel.send("カレーと言えばこの前この前携帯電話がカレーに刺さった。あまりにも見事に直立していたので、記念に撮ろうと思って携帯探したらカレーに刺さってた。")
    elif message.content == "病院":
        c=("病院と言えばこの前病院でかゆみ止めの薬をもらった。 説明書を見たら副作用に「かゆみ」と書いてあった。 効くのか、これ")
        l=client.get_channel(583932805340463104).topic
        a=[c,l]
        choice=random.choice(a)
        await message.channel.send(choice)
    elif "離婚" in message.content:
        await message.channel.send("離婚と言えば離婚の主な原因って結婚らしいぞ")
        return
    elif message.content == "いい？":
        await message.channel.send("アイアイサー")
    elif "プーさん" in message.content:
        await message.channel.send("プーさん「まずい！猟友会の奴らだ！」")
        return
    elif message.content == "犬":
        dog = ["飼ってる犬が脱走した。無事に帰ってきたのは良かったけど、おでこに「ネコ」って落書きされてた","じいちゃんが犬を捨てに行ったら、犬が先に帰ってきた。"]
        choice = random.choice(dog)
        await message.channel.send("犬と言えばこの前{}".format(choice))
        return
    elif "コンビニ" in message.content:
        ko=["コンビニで消臭剤買ったらストローついてきた。","コンビニで猫缶買ったら箸ついてきた。"]
        choice=random.choice(ko)
        await message.channel.send("話変わるけどコンビニといえばこの前{}".format(choice))
        return
    elif message.content == "１発芸":
        gei=["コンビニで猫缶買ったら箸ついてきた。","プーさん「まずい！猟友会の奴らだ！」","迷惑メールフィルターを強にしてるのに上司からメール来る"]
        choice = random.choice(gei)
        await message.channel.send(choice)
        return
    elif "ルンバ" in message.content:
        await message.channel.send("ルンバといえばこの前ばあちゃんがルンバに餌やってた")
        return
    elif "迷惑" in message.content:
        await message.channel.send("迷惑といえば迷惑メールフィルターを強にしてるのに上司からメール来る")
        return
    elif "Excel" in message.content:
        await message.channel.send("Excelといえば部長がExcelのことをエグザイルって言う…")
        return
    elif message.content == "Unknown" or message.content == "unknown":
        await message.channel.send("Unknownといえば後輩がUnknownを「うんこなう」って読んでたのでもう帰りたい。")
    elif message.content.startswith("クエ") or message.content.startswith("ぐええええ"):
        kue=["お子ちゃまは寝るわ","クワックワックワックワックワックワックワックワックワッ","クエー","くええええ","くえーー","モー","ぐわええええええ","・・・","すみません　よく分かりません","クワ！"]
        choice = random.choice(kue)
        await message.channel.send(choice)
        try:
            kue=discord.utils.get(message.guild.channels,name="kue-count")
            next=int(kue.topic)+1
            await kue.edit(topic=next)
        except AttributeError:
            return
    elif message.content.startswith("クワ"):
        kue=["お子ちゃまは寝るわ","クワックワックワックワックワックワックワックワックワッ","クエー","くええええ","くえーー","モー","ぐわええええええ","・・・","すみません　よく分かりません","クワ！"]
        choice = random.choice(kue)
        await message.channel.send(choice)
    elif message.content == "くーえー":
        kue=["お子ちゃまは寝るわ","クワックワックワックワックワックワックワックワックワッ","クエー","くええええ","くえーー","モー","ぐわええええええ","・・・","すみません　よく分かりません"]
        choice = random.choice(kue)
        await message.channel.send(choice)
    elif message.content == "えく" or message.content == "えーくー":
        c=["ねーねーそれってクエーの反対？","なにそれ","クエーの反対版かな？","クエー","うぎゅっぺぐあッ←転んだ","エクー","グワ！"]
        choice=random.choice(c)
        await message.channel.send(choice)
    elif message.content.startswith("ｸｴ"):
        kue=["お子ちゃまは寝るわ","クワックワックワックワックワックワックワックワックワッ","クエー","くええええ","くえーー","モー","ぐわええええええ","・・・","すみません　よく分かりません"]
        choice = random.choice(kue)
        await message.channel.send(choice)
    elif "チョコボール" in message.content:
        await message.channel.send("ｸｴｯヽ(･∀･｡)ﾉｸｴｯヽ(｡･∀･)ﾉｸｴｯヽ(･∀･｡)ﾉ ﾁｮｺﾎﾞｰﾙ♪")
        return
    elif message.content.startswith("くえ"):
        kue=["クワックワックワックワックワックワックワックワックワッ","クエー","くええええ","くえーー","モー","ぐわええええええ","・・・","すみません　よく分かりません"]
        choice = random.choice(kue)
        await message.channel.send(choice)
    elif message.content == "オエー":
        c=["・・・","・・・クエー","。。。","フム","、、、、","クエー","モー"]
        choice=random.choice(c)
        await message.channel.send(choice)
    elif message.content.startswith("こんばんは"):
        time=(datetime.now().hour +9)
        k=["こんばんは","クエー","こんばんは・・デス","こんばんは！","クエーーーー","クエ・・","おやすみ～","グエーーー","いらさっぁいませー"]
        k2=["( ノﾟДﾟ)おはよう","クエーおはよう","おはよ","お前はまさかあの時の村長か。おはよう","グッドモーニング","おはよ","クエーーーーー","クエッ"]
        k3=["こん","こんちゃ","こんにちは","こん・・クエー","クエー","こんちゃあ","くうぇぇ","グハッ！貴様なかなかやるな！あ、、こんちゃ","ハローここに来たから生きて帰れると思うなw"]
        if 18 <= time <= 5:
            choice=random.choice(k)
            await message.channel.send(choice)
        elif 6 <= time <= 12:
            choice=random.choice(k2)
            await message.channel.send(choice)
        elif 13 <= time <= 17:
            choice=random.choice(k2)
            await message.channel.send(choice)
        else:
            choice=random.choice(k3)
            await message.channel.send(choice)
    elif message.content.startswith("おはよ") or message.content == "おは" or message.content == "おっはー" or message.content == "おっは" or message.content == "おっはよ" or message.content == "おっはよ～":
        p=(datetime.now().hour + 10)
        oha=["おはようございます。朝日がきれいですね。","おはよ","おはよう","クエー","おはようです","おはようでござる","おはようクエー"]
        oha2=["もう昼ですね","おそよう","起きるの遅いですね","おはようございます。太陽が輝いてますね。もう{}時です".format(h)]
        oha3=["遅いですね","太陽傾いてるけど","おそすぎ","夕日がきれいですね。おはようございます","おはよう。いやおそよう","もう{}時だよ".format(h)]
        oha4=["うん、もう夜だよね","もう夜だ。( ノﾟДﾟ)おはよう","星がきれいですね","おやすみ","今{}時・・おはよ".format(h)]
        oha5=["はやいのか遅いのか","朝焼けがきれいですね","起きるの早いですね","昼と夜逆転してませんか？","もう{}時だけど".format(h)]
        oha6=["おはよう！早起きだね","おはようございます！早起きは3文の得！","こんなに早く起きれるなんてうらやましいわ","おっはー","( ノﾟДﾟ)おはよう"]
        if 6 <= (datetime.now().hour +9) < 9:
            choice = random.choice(oha)
            await message.channel.send(choice)
        elif 9 <= (datetime.now().hour + 9) < 13:
            choice = random.choice(oha2)
            await message.channel.send(choice)
        elif 13 <= (datetime.now().hour + 9) <15:
            choice = random.choice(oha3)
            await message.channel.send(choice)
        elif 15 <= (datetime.now().hour + 9) <24:
            choice = random.choice(oha4)
            await message.channel.send(choice)
        elif 24 <= (datetime.now().hour + 9) <4:
            choice = random.choice(oha5)
            await message.channel.send(choice)
        elif 4 <= (datetime.now().hour + 9) <6:
            choice=random.hoice(oha6)
            await message.channel.send(choice)
        else:
            choice=random.choice(oha)
            await message.channel.send(choice)
    elif "魔法の言葉" in message.content:
        await message.channel.send("家がちらかる魔法の言葉「何かに使えるかもしれない」")
        return
    elif "チンパンジー" in message.content:
        await message.channel.send("チンパンジーから怪人パンチ")
        return
    elif "影武者" in message.content:
        await message.channel.send("影武者「ハハハ！馬鹿め！そっちが本物だ！」")
    elif message.content == "おそよう":
        h=datetime.now().hour
        if 6 <= h < 8:
            await message.channel.send("8時前の{}時だしまあ普通じゃない？".format(h))
        elif 8 <= h < 10:
            await message.channel.send("{}時か、一応朝かな".format(h))
        elif 10 <= h < 12:
            await message.channel.send("お昼の{}時だ。おそよう".format(h))
        elif 12 <= h < 14:
            await message.channel.send("おそよう。{}時ですよもう".format(h))
        elif 14 <= h < 15:
            await message.channel.send("もう{}時、おやつの時間だ！".format(h))
        elif 15 <= h < 17:
            await message.channel.send("夕方の{}時ですか。おそよう".format(h))
        elif 17 <= h < 20:
            await message.channel.send("{}時だけどおそよう。君の一日はこれからかな？".format(h))
        elif 20 <= h < 24:
            await message.channel.send("・・・もう{}時だから寝ようね".format(h))
        elif 1 <= h < 5:
            await message.channel.send("{}時に起きるって早起きなのか寝坊なのか".format(h))
        else:
            c=["おそよお！","おそよ","クエー","おそよっす","クワ―","クエーーー","おそよおです"]
            choice=random.choice(c)
            await message.channel.send(choice)
    elif message.content == "攻撃！":
        await message.channel.send("１２００ダメージもくらったぞ")
    elif "パンいち" in message.content:
        await message.channel.send("風邪ひくよ")
    elif "復活しろ" in message.content:
        await message.channel.send("教会で復活してゴールド半分取られたわ")
    elif message.content.startswith("ニート"):
        await message.channel.send("働いたら負けだ")
    elif message.content == "眠い":
        ne4=["暇なら寝れば","ちょっと早いけどいいんじゃね","おやすみ"]
        ne=["寝れば？","おこちゃまは寝る時間","寝ろ","おやすみ"]
        ne2=["まだ朝だけど","はええよ","クエー","２度寝したら？"]
        ne3=["お昼寝したら？","昼だけど","クエー","今{}時だよ".format(h)]
        ne5=["２度寝すれば？","もう１回寝ろ","でしょうね"]
        if 7 <= (datetime.now().hour + 9) < 12:
            choice = random.choice(ne2)
            await message.channel.send(choice)
        elif 12 <= (datetime.now().hour + 9) < 17:
            choice = random.choice(ne3)
            await message.channel.send(choice)
        elif 17 <= (datetime.now().hour + 9) < 19:
            choice = random.choice(ne4)
            await message.channel.send(choice)
        elif 19 <= (datetime.now().hour + 9) < 24:
            choice = random.choice(ne)
            await message.channel.send(choice)
        elif 0 <= (datetime.now().hour + 9) < 7:
            choice = random.choice(ne5)
            await message.channel.send(choice)   
        else:
            choice=random.choice(ne)
            await message.channel.send(choice)
    elif "食べたい" in message.content:
        if "寿司" in message.content:
            c=["寿司僕も食べたい","うむわかる","うむ","クエー","わかる","ふむ","くうう","お腹すいてきた","🍣"]
            choice=random.choice(c)
            await message.channel.send(choice)
            return
        elif "ご飯" in message.content:
            c=["お腹すいたね","うむ","クエー","うわん！","ふぇえええ"]
            choice=random.choice(c)
            await message.channel.send(choice)
            return
    elif message.content == "ユーザーのアイコン":
        await message.channel.send(message.author.avatar_url)
    elif message.content.startswith("サーバーのアイコン"):
        await message.channel.send(message.guild.icon_url)
    elif message.content == "こんにちは":
        he=["こん","こんにちは",m+"さん、こんにちは","こんにちは今日はいい天気ドスな","クエー","さぁゲームを始めようか","地獄の底から這い上がって来たぞ","お前はまさかあの時の村長か","ハローここに来たから生きて帰れると思うなw"]
        choice=random.choice(he)
        await message.channel.send(choice)
    elif message.content == "こん":
        he=["こん","こんにちは",m+"さん、こんにちは","こんにちは今日はいい天気ドスな","クエー","さぁゲームを始めようか","地獄の底から這い上がって来たぞ","お前はまさかあの時の村長か","ハローここに来たから生きて帰れると思うなw"]
        choice=random.choice(he)
        await message.channel.send(choice)
    elif message.content == "konn":
        he=["こん","こんにちは",m+"さん、こんにちは","こんにちは今日はいい天気ドスな","クエー","さぁゲームを始めようか","地獄の底から這い上がって来たぞ","お前はまさかあの時の村長か"]
        choice=random.choice(he)
        await message.channel.send(choice)
    elif message.content == "kon":
        he=["こん","こんにちは",m+"さん、こんにちは","こんにちは今日はいい天気ドスな","クエー","さぁゲームを始めようか","地獄の底から這い上がって来たぞ","お前はまさかあの時の村長か"]
        choice=random.choice(he)
        await message.channel.send(choice)
    elif message.content.startswith("待"):
        await message.channel.send("３分間だけまってやろう")
    elif message.content == "おい":
        oi = ["僕は思考能力もあるし格が違うんだよ。","お前はまさかあの時の村長か","すみません　よく分かりません","グハッまさか勇者だと","これで全力か？","お前の目は節穴か","クエー","兵隊さんの悪い癖だ"]
        choice = random.choice(oi)
        await message.channel.send(choice)
    elif "行く" in message.content:
        if message.author.bot:
            return
        iku = ["イッテラ","イッテラサァイ","いらさっあい","いってらっしゃいませ","行ってくるがよい"]
        choice = random.choice(iku)
        await message.channel.send(choice)
        return
    elif message.content == 'あっ、あれは':
        if message.author.bot:
            return
        await message.channel.send('ふはははっはは　ひれふせ下民どもぉ{}様のおとおりだあ'.format(client.user.mention))
    elif "行ってきます" in message.content:
        if message.author.bot:
            return
        iku = ["イッテラ","イッテラサァイ","いらさっあい","いってらっしゃいませ","行ってくるがよい"]
        choice = random.choice(iku)
        await message.channel.send(choice)
        return
    elif "お腹すいた" in message.content or "お腹空いた" in message.content:
        if message.author.bot:
            return
        c=["クエ・・","俺も","クワ！","お腹空いたね","うむ","わかる","クエ","ぎゃうん","ふぉええ","ぐ～←お腹の音"]
        await message.channel.send(random.choice(c))
        return
    elif "いってきます" in message.content:
        if message.author.bot:
            return
        iku = ["イッテラ","イッテラサァイ","いらさっあい","いってらっしゃいませ","行ってくるがよい"]
        choice = random.choice(iku)
        await message.channel.send(choice)
        return
    elif message.content == "ご飯":
        if message.author.bot:
            return
        iku = ["イッテラ","イッテラサァイ","いらさっあい","いってらっしゃいませ","行ってくるがよい"]
        choice = random.choice(iku)
        await message.channel.send(choice)
    elif message.content == "ただいま":
        c=["おかえり","おかえりでござる","クエー","おかえりなさいぃ","うぎゅええ←出迎えようとして転んだ","おかえりなさい～でござる","待ってましたぁ！"]
        choice=random.choice(c)
        await message.channel.send(choice)
    elif "寝" in message.content:
        oti = ["おやすみでござる","いい夢みろよ","バイバイきん","おやすみ","クエー","さっさと寝るがよい","そのまま永遠に眠るがよい（...ネタですごめんなさい）","すみません　よく分かりません","３分間だけまってやろう。おやすみ","４０秒で支度しな！"]
        choice = random.choice(oti)
        await message.channel.send(choice)
        return
    elif message.content.startswith("おやすみ"):
        oti = ["おやすみでござる","いい夢みろよ","バイバイきん","おやすみ","クエー","さっさと寝るがよい","そのまま永遠に眠るがよい（...ネタですごめんなさい）","すみません　よく分かりません","３分間だけまってやろう。おやすみ","４０秒で支度しな！"]
        choice = random.choice(oti)
        await message.channel.send(choice)
        return
    elif message.content.startswith("oyasumi"):
        oti = ["おやすみでござる","いい夢みろよ","バイバイきん","おやすみ","クエー","さっさと寝るがよい","そのまま永遠に眠るがよい","すみません　よく分かりません","３分間だけまってやろう。おやすみ"]
        choice = random.choice(oti)
        await message.channel.send(choice)
        return
    elif message.content.startswith("この剣"):
        sw=["まさかその剣は天叢雲剣か","まさかその剣はエクスカリバーか","レベル３２の我を倒せるものなら倒してみろ","グハッまさか勇者だと"]
        choice=random.choice(sw)
        await message.channel.send(choice)
        return
    elif message.content.startswith("世の中"):
        await message.channel.send("いや、世の中筋肉")
        return
    elif message.content == "あけおめ":
      if datetime.now().month == 1:
        if datetime.now().day == 1:
            nw=["元日おめでとう","お年玉くれ","{}年もよろしく！".format(datetime.now().year)]
            choice=random.choice(nw)
            await message.channel.send(choice)
        else:
            nw=["あけおめ","あけましておめでとお","{}年もよろしく！".format(datetime.now().year)]
            choice=random.choice(nw)
            await message.channel.send(choice)
      else:
        nw=["まだだろ","まだ{}年".format(datetime.now().year),"正月に近くもない。でもお年玉くれ","まだ{}月だね".format(datetime.now().month)]
        choice=random.choice(nw)
        await message.channel.send(choice)
    elif message.content.startswith("カップラーメン"):
        await message.channel.send("３分間だけまってやろう")
    elif "借金ある" in message.content:
        await message.channel.send("借金「これから、ずっと一緒だよ…。」")
        return
    elif "マヨネーズ" in message.content:
        await message.channel.send("俺くらいのマヨラーになると、マヨネーズなしでご飯が食える")
        return
    elif message.content == "サイコロ振って":
        dice=["1","2","3","4","5","6"]
        c=random.choice(dice)
        await message.channel.send("`{}`が出たお！".format(c))
    elif message.content == "ぴよ":
        piyo=["ひよこかよ","ピヨピヨ","クエー","ぴよ"]
        choice=random.choice(piyo)
        await message.channel.send(choice)
    elif message.content == "風呂":
        fu=["いってらっしゃい","我は金の風呂にいつも入るのじゃ。嘘だけど","風呂♪風呂♪","お風呂がわきました～","クエーいいなー","**押忍**"]
        choice=random.choice(fu)
        await message.channel.send(choice)
    elif "ストーカー" in message.content:
        await message.channel.send("ストーカーと言えば俺の友達が毎日見守ってる女の子がストーカーにあってるらしい")
        return
    elif message.content == "誕生日プレゼント":
        await message.channel.send("誕プレと言えば姪の誕生日に｢これで何か美味しいものでも食べなさない。｣って割り箸あげました。")
    elif message.content == "わかる":
        c=["","すみません　よく分かりません","君は思考能力もあるし格が違うんだよ。","謎すぎる"]
        msg=random.choice(c)
        await message.channel.send(msg)
    elif "アンパンマン" in message.content:
        await message.channel.send("「アンパンマンは君さ」という真実を告げられた時の衝撃")
        return
    elif message.content == "今日何日？" or message.content == "日付は？":
        y=datetime.now().year
        m=datetime.now().month
        d=datetime.now().day
        c=["うーんと","えーと","えーオホン！","うん？","Yes SIR！","ほいほい","調べる...えー","~~知るか！~~"]
        choice=random.choice(c)
        await message.channel.send("{}今は{}年の{}月{}日だね".format(choice,y,m,d))
    elif message.content == "時間は？" or message.content == "いま何時？":
        y=datetime.now().year
        m=datetime.now().month
        d=datetime.now().day
        h=datetime.now().hour + 9
        mi=datetime.now().minute
        s=datetime.now().second
        await message.channel.send("今は{}年の{}月{}日{}時{}分{}秒だね".format(y,m,d,h,mi,s))
    elif message.content == "今何時？":
        y=datetime.now().year
        m=datetime.now().month
        d=datetime.now().day
        h=datetime.now().hour + 9
        mi=datetime.now().minute
        s=datetime.now().second
        await message.channel.send("今は{}年の{}月{}日{}時{}分{}秒だね".format(y,m,d,h,mi,s))
    elif message.content.startswith("地獄に"):
        await message.channel.send("地獄の底から這い上がって来たぞ")
    elif message.content == "わからん":
        c=["お前の目は節穴か","僕は思考能力もあるし格が違うんだよ","寝るが良い","すみません 私にもよくわかりません"]
        msg=random.choice(c)
        await message.channel.send(msg)
    elif message.content == "モー":
        moo = ["モー","もー","牛？","クエー"]
        choice = random.choice(moo)
        await message.channel.send((choice))
    elif message.content.startswith("うらめしや"):
        await message.channel.send("化物め退治してくれるわ")
    elif message.content == "レベル１００":
        await message.channel.send("グッハ　まさかお前レベル３２のゴブリンより強いのか")
    elif "田中" in message.content:
        if message.author.bot:
            return
        await message.channel.send("中1の時、学年中の靴箱の「田中」を「油虫」にして 校長室に呼ばれた")
        return
    elif "Death Note" in message.content:
        if message.author.bot:
            return
        await message.channel.send("この前拾った黒いノートを日記にしてたら友達がいっぱい死んだ")
        return
    elif "日本の未来" in message.content:
        if message.author.bot:
            return
        await message.channel.send("日本の官公庁の中で本気で明日の日本のこと考えてるのって、どこだと思う？\n俺「気象庁位だろ」")
        return
    elif "千利休" in message.content:
        if message.author.bot:
            return
        await message.channel.send("弟子「疲れました先生」\n千利休「せやな。とりあえずどっかのカフェでコーヒーでも飲もう」")
        return
    elif "桃太郎" in message.content:
        if message.author.bot:
            return
        await message.channel.send("おばあさん「洗濯機買うたで」")
        return
    elif message.content == "簡単":
        await message.channel.send("え..簡単...? {}ってまさかプロ..?".format(message.author.mention))
    elif "お疲れ" in message.content or message.content == "おつかれ":
        c=["おつかれぃ！","おつかれさま～","おつかれさまでーす","クエーおつかれ","お疲れ様でござる","おつかれぃでござる","お疲れさま～","ふぇえおつかれえ","カツカレー"]
        choice=random.choice(c)
        await message.channel.send(choice)
        return
    elif message.content == "疲れた" or message.content == "つかれた" or message.content == "おつ":
        c=["おつかれ～","お疲れさまでござる","お疲れ！","クエー","お疲れ様です。","{}さん、お疲れ～".format(message.author.name)]
        choice=random.choice(c)
        await message.channel.send(choice)
    elif message.content == "うむ" or message.content == "そうだな":
        c=["フム","なるほど","うむ","そうだな","クエー","ねえ、話変わるけどメロンパン食べたい","たしかに","ふぇえ"]
        choice=random.choice(c)
        await message.channel.send(choice)
    elif message.content == "ども":
        c=["ども","どーも","ドモドモ","クエードーモ","ドモデス","こんちゃあ","クエー","うわっほい。ども","ひょええん。ども"]
        choice=random.choice(c)
        await message.channel.send(choice)
    elif message.content == "ニュース作って":
        fakenews = ["校長先生のかつら","某スマホゲームで課金アイテム", "０点のテスト答案を鼻をかむティッシュとして", "学校で１年ほど洗っていない上靴を","テスト勉強中に携帯","修学旅行で一人だけプライベートジェット","友達３人とマクドナルドに行った際、一人だけクーポン","ママのへそくり","パパの大事なゴルフクラブ","学校二階奥の教師用男子便所","テスト中にカンニング方法を検索するためにスマホ"]
        choice = random.choice(fakenews)
        f_news=""
        f_news+="{}容疑者\n".format(message.author)
        f_news+="{}を使用した疑いで逮捕。\n教師側の調べに対して\n".format(choice)
        fakenews2 = ["私はやっていない", "違うんだぁ", "あれは俺のせいじゃない！", "弁護士を呼んでください","あなたにはわからないでしょうねぇ！","そんなことよりおうどん食べたい","僕は無罪だぁ","仕方がなかったんだ","UFOが出てきて…","はめられたんだ","証拠はあるのか","黙秘権を行使する","あぁぁぁぁぁ誰がやっても同じやと思てぇぇぇ"]
        choice = random.choice(fakenews2)
        f_news+="「{}」\nなどと供述し、容疑を否認しています。".format(choice)
        await message.channel.send(f_news)
    elif message.content == "悲報作って":
        sigfake = ["あんパンを買うも、中身が入ってなかった", "課金アイテムを買った瞬間iPhone水没","宝くじをあてるもなくす","１００点をテストでとるも、なくし結局怒られる","５０％引きのお得商品を急いで取ろうとして指を突き指"]
        choice = random.choice(sigfake)
        f_news="【悲報】\n{}氏\n{}".format(message.author,choice)
        await message.channel.send(f_news)
    elif message.content == '朗報作って':
        sigfake = ["が家出。行先や期間は不明", "が女性だということを政府が公表","が動物園から脱走\n近隣住民の方は気を付けてください","が独立を宣言","が行方不明となる。見つけたら１１０番","無料版の配信がスタート","が財布を落とす","宝くじを当てるもなくす\nなお金額は300円の模様"]
        choice = random.choice(sigfake)
        choice = random.choice(sigfake)
        f_news="【朗報】\n{}{}".format(message.author,choice)
    elif message.content == '猫の学名':
        await message.channel.send('猫の学名は`Felis catus`\nこの機能いる...?')
    elif message.content == '犬の学名':
        await message.channel.send('犬の学名は`Canis lupus familiaris`\nこの機能いる...?')
    elif message.content == "ぴ":
        await message.channel.send("ぴ・・・？")
    elif message.content.startswith("ピカソの本名"):
        await message.channel.send("ピカソの本名はたしか```パブロ・ディエゴ・ホセ・フランシスコ・デ・パウラ・ファン・ネポムセーノ・マリア・デ・ロス・レメディオス・クリスピン・クリスピアーノ・デ・ラ・サンティシマ・トリニダード・ルイス・イ・ピカソ```だったよね～。\nこれ常識だよね～。")
  
  client.run(discord_token)
