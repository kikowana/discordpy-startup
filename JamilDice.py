import discord
import random

TOKEN = 'Nzk4ODU1OTU2MzMwMzE1ODQ2.X_7Glg.5DJnxB-AHubjuPhXjyVHagVKC0o'

clint = discord.Client()


@clint.event
async def on_ready():
    print('ログインしました')

@clint.event
async def on_message(message):
    if message.author.bot:
        return

    say = message.channel.send
    msg = message.content

    user_id1 = message.author
    user_id2 = str(user_id1).split("#")
    user = str(user_id2[0])

    try :
        loot = str(msg).replace("r","")#r100v50が100v50
        num = loot.split("v") #num[0],num[1]の取得
        if msg == "r{}v{}".format(str(num[0]),str(num[1])) :
            dice = random.randint(1,int(num[0]))
            if dice <= int(num[1]):
                if int(num[0]) == 100 and dice <= 5 :
                    await say("結果:"+str(dice)+"  決定的な成功だな。")
                    await say('うん、なかなかだ。')

                else :
                    await say("結果："+str(dice)+"  成功だな。")

            elif dice >= int(num[1]):
                if int(num[0]) == 100 and dice >= 96 :
                    await say("結果："+str(dice)+"  ...致命的な失敗だ。")
                    await say('これは気が抜けないな。')

                else :
                    await say("結果："+str(dice)+"  失敗したな。")

    except IndexError:
        loot = str(msg).replace("r","")#r100v50が100v50
        if msg == "r{}".format(str(loot)) :
            dice = random.randint(1,int(loot))
            if int(loot) == 100 and dice <= 5 :
                await say("結果："+str(dice)+"  決定的な成功だな。")
                await say('次もこの調子だと助かるんだがな。')

            elif int(loot) == 100 and dice >= 95 :
                await say("結果："+str(dice)+"  ...致命的な失敗だ。")
                await say(str(user)+"もダイスに振り回されて大変だな。")

            elif dice <= int(loot)/2 :
                 await say("結果："+str(dice)+"  悪くないな。")

            elif dice >= int(loot)/2 :
                await say("結果："+str(dice)+"  少し不安だな。")

    except ValueError:
        pass

    try:
        roll = str(msg).split("r")#2r100 =>2,100 roll[0],roll[1]
        if msg == "{}r{}".format(str(roll[0]),str(roll[1])):
            x = int(roll[0])
            total = []
            while x != 0:
                result = random.randint(1,int(roll[1]))
                total.append(int(result))
                x -= 1
                if x == 0:
                    a = sum(total) #合計
                    b = int(roll[1]) / 2
                    if int(a) > int(int(b)*int(roll[0])):
                        await say("結果：{}".format(str(total)))
                        await say("合計：{} なかなか高いな。".format(str(a)))

                    elif int(a) <= int(int(b)*int(roll[0])):
                        await say("結果：{}".format(str(total)))
                        await say("合計：{} 低めの値だな。".format(str(a)))

    except IndexError:
        pass
             
    except ValueError:
        pass

    if msg == "jamil占い":
        result = ["大吉","中吉","末吉","吉","小吉","凶","大凶"]

        omikuji = random.choice(result)

        await say(str(user)+"の運勢は"+ omikuji + "だ。")

        if omikuji == '大吉':
            await say("何をやってもいいが面倒だけは起こしてくれるなよ。")

        if omikuji == '中吉':
            await say('悪くないな。')

        if omikuji == '末吉':
            await say('慎重に、正確に。')
            await say('そうすれば失敗なんかしようがない。')

        if omikuji == '吉':
            await say('可もなく不可もなくだな。')
            await say('いたって普通だな。')

        if omikuji == '小吉':
            await say('面倒ごとはごめんだぞ。')

        if omikuji == '凶':
            await say('さて、今日も一日気が抜けないな。')

        if omikuji == '大凶':
            await say('...今日は外出は控えたらどうだ？')
            await say('怪我だけはするなよ。')

    if msg == 'jamilおはよう' :
        pattern = [1,2,3]
        x = random.choice(pattern)

        if x == 1 :
            await say("騒がしいと思えば..."+str(user)+"か。")
            await say("おはよう。")

        if x == 2:
            await say("...おはよう、といってももう8時だが。よくそんな時間まで"+str(user)+"は寝ていられるな。")
            await say("君の間抜けな寝顔を見ていると自分の悩みなんてどうでもよくなるよ、ははは")

        if x == 3:
            await say("ああ、おはよう{}。俺もちょうど今起きたところだ。".format(str(user)))
            await say("今日も平和に過ごしたいものだな。")

    if msg == 'jamilおやすみ' :
        pattern = [1,1,2,2,3]
        x = random.choice(pattern)

        if x == 1 :
            await say("........おやすみ。まあ俺はいまから洗い物をして洗濯をしてカリムの明日の朝ごはんと弁当の仕込みをしてカリムを寝かしつけて勉強するがな、ははは。")
            await say("...もう一度言う、おやすみ"+str(user)+"。")

        elif x == 2 :
            await say("ああ、おやすみ。")
            await say("今日は俺も早く寝るか。....おやすみ"+str(user)+"。")

        elif x == 3 :
            await say("......zzz")

    if msg == "jamilcall":
        pattern = [1,2,3]
        x = random.choice(pattern)

        if x == 1 :
            await say("..."+str(user)+"。これで満足か？")

        elif x == 2 :
            await say(str(user)+"か。いちいち俺を呼ぶな。")

        elif x == 3 :
            await say("俺に何か用か？いま忙しいんだ。")
            await say("後にしてくれ。")

    try :
        Jp = msg.replace("jamilgame/","")
        Jp = str(Jp)
        if msg == "jamilgame/{}".format(str(Jp)) :
            Jj = random.randint(1,3)

            if str(Jp) == "グー": #player=グー
                Jp = 2
                if int(Jp) == Jj :#グー対チョキ
                    await say(str(user)+"：グー　Jamil：チョキ")
                    await say("俺の負けのようだな。")

                elif int(Jp) < Jj :#グー対パー
                    await say(str(user)+"：グー　Jamil：パー")
                    await say("俺の勝ちだな。")
                    await say("俺と遊んでいる余裕なんてあるのか？")

                else:#グー対グー
                    await say(str(user)+"：グー　Jamil：グー")
                    await say("引き分け...いや、この国ではあいこと言うんだったな。")

            if str(Jp) == "パー": #player=パー
                Jp = 2
                if int(Jp) > Jj :#パー対グー
                    await say(str(user)+"：パー　Jamil：グー")
                    await say("俺の負けのようだな。")

                elif int(Jp) == Jj :#パー対チョキ
                    await say(str(user)+"：パー　Jamil：チョキ")
                    await say("俺の勝ちだな。")
                    await say("俺と遊んでいる余裕なんてあるのか？")

                else:#パー対パー
                    await say(str(user)+"：パー　Jamil：パー")
                    await say("引き分け...いや、この国ではあいこと言うんだったな。")

            if str(Jp) == "チョキ": #player=チョキ
                Jp = 2
                if int(Jp) < Jj :#チョキ対パー
                    await say(str(user)+"：チョキ　Jamil：パー")
                    await say("俺の負けのようだな。")

                elif int(Jp) > Jj :#チョキ対グー
                    await say(str(user)+"：チョキ　Jamil：グー")
                    await say("俺の勝ちだな。")
                    await say("俺と遊んでいる余裕なんてあるのか？")

                else:#チョキ対チョキ
                    await say(str(user)+"：チョキ　Jamil：チョキ")
                    await say("引き分け...いや、この国ではあいこと言うんだったな。")

    except ValueError:
        pass  

    if msg == "jamilhelp":
        pattern = [1,2]
        result = random.choice(pattern)
        if result == 1:
            await say("緊張するのはわかるが、落ち着け。{}。".format(str(user)))
            await say("ほら、深呼吸……どうだ。")
            await say("少しは冷静になったか？")

        if result == 2:
            await say("なんだ、そわそわして。")
            await say("君はもっと胸を張ったほうがいいな。")
            await say("式典服に負けてしまうぞ。")

    if msg == "hey jamil":
        await say("すいません。")
        await say("よくわかりません。(CV.siri)")

    try:
        siri = msg.replace("hey jamil ","")#hey jamil 歌って　=> 歌って
        if siri == "歌って":
            pattern = [1,1,2]
            result = random.choice(pattern)
            if result == 1:
                await say("歌えません。(CV.siri)")

            elif result == 2:
                await say("少しだけだぞ。")
                await say(".....")
                if result == 2:
                    await say("ねじれた　リズムで踊ろう")
                    await say("俯き張る　意地も愛嬌さ")
                    await say("問題(かまわ)ないよ")
                    await say("ちょっとワルいくらいがいいじゃない？")
                    await say("{}。これで満足か？".format(str(user)))

    except ValueError:
        pass

    if msg == "/help":
        a = ["占い","おはよう","おやすみ","help","call"]
        b = ["グー","チョキ","パー"]
        await say("対応可能なコマンド一覧だ。")
        await say("jamil[a],a={}".format(str(a)))
        await say("jamilgame/[b],b={}".format(str(b)))


           
           
   

clint.run(TOKEN)