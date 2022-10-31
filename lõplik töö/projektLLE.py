import PySimpleGUI as sg

sg.theme('Purple')

# loome loendid vastuste kokku arvutamiseks
valik_A = 0 #alati hea vastus
valik_B = 0 #alati halb vastus


# loome akna
# näide sulle kuidas tekst teistel küsimustel välja võiks näha


paigutus0 = [[sg.Graph(
            canvas_size =(800, 600),
            graph_bottom_left=(0, 800),
            graph_top_right=(800, 0),
            key="lõuend")],
            [sg.Button('START')],
            [sg.Cancel('Välju')]]


aken = sg.Window("SINA!", paigutus0)
aken.Finalize()
minu_lõuend = aken.Element("lõuend")
start = minu_lõuend.DrawImage(filename="start.png", location=(0, 0))




# loome tegevused
while True:
    syndmus0, v22rtused0 = aken.Read()

    # sulge programm, kui vajutatakse Välju või suletakse aken X-st
    if syndmus0 == "Välju" or syndmus0 == sg.WIN_CLOSED:
        aken.close()
        break
    if syndmus0 == "START":
        aken.close()
        
        
        paigutus01 = [[sg.Graph(
            canvas_size =(800, 600),
            graph_bottom_left=(0, 800),
            graph_top_right=(800, 0),
            key="lõuend")],
            [sg.Text('Sul on valikus kolm erinevat mängu.')],
            [sg.Button('Suhted'), sg.Text('Saa teada, kas Sinu suhe on toksiline!')],
            [sg.Button('Sõbrad'), sg.Text('Saa teada, kuidas sõbrad Sind mõjutavad!')],
            [sg.Button('Sina'), sg.Text('Saa teada, kas Sul esineb probleeme!')],
            [sg.Cancel('Välju')]]
    
        aken = sg.Window("SINA!", paigutus01)
        aken.Finalize()
        minu_lõuend = aken.Element("lõuend")
        taustapilt = minu_lõuend.DrawImage(filename="valik1.png", location=(0, 0))
        
    
        syndmus01, v22rtused01 = aken.Read()
            
        if syndmus01 == "Välju" or syndmus01 == sg.WIN_CLOSED:
            aken.close()
            break
        if syndmus01 == "Sõbrad":
            aken.close()
            
           
           
            paigutus1 = [[sg.Graph(
                canvas_size =(800, 600),
                graph_bottom_left=(0, 800),
                graph_top_right=(800, 0),
                key="lõuend")],
                [sg.Text('Sa ostad endale uued püksid ja näitad neid oma sõbrale.')],
                [sg.Text('Kuidas reageerib sellele su sõber?')],
                [sg.Button('A'), sg.Text('A: Oi kui ilusad püksid! Need sobivad sulle nii hästi!')],
                [sg.Button('B'), sg.Text('B: Iu kui kole sa välja näed. Sa peaksid need tagastama!')],
                [sg.Cancel('Välju')]]
        
            aken = sg.Window("SÕBRAD!", paigutus1)
            aken.Finalize()
            minu_lõuend = aken.Element("lõuend")
            taustapilt = minu_lõuend.DrawImage(filename="taustsober.png", location=(0, 0))
            
        
            syndmus1, v22rtused1 = aken.Read()

            # sulge programm, kui vajutatakse Välju või suletakse aken X-st
            if syndmus1 == "Välju" or syndmus1 == sg.WIN_CLOSED:
                aken.close()
                break
            if syndmus1 == "A" or syndmus1 == "B":
                aken.close()

                if syndmus1 == "A":
                    valik_A += 1
                if syndmus1 == "B":
                    valik_B += 1
                
                # loome akna uue järjendiga
                paigutus2 = [[sg.Graph(
                    canvas_size =(800, 600),
                    graph_bottom_left=(0, 800),
                    graph_top_right=(800, 0),
                    key="lõuend")],
                    [sg.Text('Sa oled oma sõbraga kohvikus ja mõtled mida tellida')],
                    [sg.Text('Sina: "Hmm, ma tahan vist friikartulid tellida"')],
                    [sg.Text('Kuidas vastab su sõber?')],
                    [sg.Button('A'), sg.Text('See on väga hea mõte! Ma võtan sama.')],
                    [sg.Button('B'), sg.Text('Sa peaksid küll salatit rohkem sööma. Vaata, milline sa välja näed!')],
                    [sg.Cancel('Välju')]]
                
                aken = sg.Window("SÕBRAD!", paigutus2)
                aken.Finalize()
                minu_lõuend = aken.Element("lõuend")
                taustapilt = minu_lõuend.DrawImage(filename="taustsober.png", location=(0, 0))
                
                syndmus2, v22rtused2 = aken.read()

                if syndmus2 == "Välju" or syndmus2 == sg.WIN_CLOSED:
                    aken.close()
                    break
                if syndmus2 == "A" or syndmus2 == "B":
                    aken.close()

                    if syndmus2 == "A":
                        valik_A += 1
                    if syndmus2 == "B":
                        valik_B += 1

                    # loome akna uue järjendiga
                    paigutus3 = [[sg.Graph(
                        canvas_size =(800, 600),
                        graph_bottom_left=(0, 800),
                        graph_top_right=(800, 0),
                        key="lõuend")],
                        [sg.Text('Sa pole oma sõpra 2 nädalat näinud ja helistad talle, et kokku saada.')],
                        [sg.Text('Mida arvab sellest mõttest su sõber?')],
                        [sg.Button('A'), sg.Text('Pole tõesti kaua näinud. Muidugi tahan ma sinuga kokku saada!')],
                        [sg.Button('B'), sg.Text('Mul pole kogu aeg sinuga aega tegeleda. Ma saan sinu asemel täna hoopis mimmuga kokku.')],
                        [sg.Cancel('Välju')]]
                    
                    aken = sg.Window("SÕBRAD!", paigutus3)
                    aken.Finalize()
                    minu_lõuend = aken.Element("lõuend")
                    taustapilt = minu_lõuend.DrawImage(filename="taustsober.png", location=(0, 0))
                    
                    syndmus3, v22rtused3 = aken.read()

                    if syndmus3 == "Välju" or syndmus3 == sg.WIN_CLOSED:
                        aken.close()
                        break
                    if syndmus3 == "A" or syndmus3 == "B":
                        aken.close()

                        if syndmus3 == "A":
                            valik_A += 1
                        if syndmus3 == "B":
                            valik_B += 1

                        # loome akna uue järjendiga
                        paigutus4 = [[sg.Graph(
                            canvas_size =(800, 600),
                            graph_bottom_left=(0, 800),
                            graph_top_right=(800, 0),
                            key="lõuend")],
                            [sg.Text('Sa kukutad kogemata oma sõbra juures kausi maha ja see läheb katki.')],
                            [sg.Text('Kuidas reageerib su sõber?')],
                            [sg.Button('A'), sg.Text('Oi pole hullu! Ma aitan sul killud ära koristada.')],
                            [sg.Button('B'), sg.Text('Mis sul viga on! Kas sa oled mingi titt, kes ei suuda asju normaalselt käes hoida vä!?')],
                            [sg.Cancel('Välju')]]
                        
                        aken = sg.Window("SÕBRAD!", paigutus4)
                        aken.Finalize()
                        minu_lõuend = aken.Element("lõuend")
                        taustapilt = minu_lõuend.DrawImage(filename="taustsober.png", location=(0, 0))
                        
                        syndmus4, v22rtused4 = aken.read()

                        if syndmus4 == "Välju" or syndmus4 == sg.WIN_CLOSED:
                            aken.close()
                            break
                        if syndmus4 == "A" or syndmus4 == "B":
                            aken.close()

                            if syndmus4 == "A":
                                valik_A += 1
                            if syndmus4 == "B":
                                valik_B += 1

                            # loome akna uue järjendiga
                            paigutus5 = [[sg.Graph(
                                canvas_size =(800, 600),
                                graph_bottom_left=(0, 800),
                                graph_top_right=(800, 0),
                                key="lõuend")],
                                [sg.Text('Sa sõidutad oma sõbra iga päev kooli ja koolist koju. Ühel päeval on su auto aga katki ja palud hoopis')],
                                [sg.Text('oma sõbralt sõitu.')],
                                [sg.Text('Mida vastab su sõber?')],
                                [sg.Button('A'), sg.Text('Muidugi võin ma su peale võtta! Sa sõidutad ju mind iga päev.')],
                                [sg.Button('B'), sg.Text('Ma ei viitsi sinu juurest läbi sõita. Vaata ise kuidas kooli saad.')],
                                [sg.Cancel('Välju')]]
                            
                            aken = sg.Window("SÕBRAD!", paigutus5)
                            aken.Finalize()
                            minu_lõuend = aken.Element("lõuend")
                            taustapilt = minu_lõuend.DrawImage(filename="taustsober.png", location=(0, 0))
                            
                            syndmus5, v22rtused5 = aken.read()

                            if syndmus5 == "Välju" or syndmus5 == sg.WIN_CLOSED:
                                aken.close()
                                break
                            if syndmus5 == "A" or syndmus5 == "B":
                                aken.close()

                                if syndmus5 == "A":
                                    valik_A += 1
                                if syndmus5 == "B":
                                    valik_B += 1
                            
                            
                            if str(valik_A) < str(valik_B):
                                paigutus6 = [[sg.Graph(
                                    canvas_size =(800, 600),
                                    graph_bottom_left=(0, 800),
                                    graph_top_right=(800, 0),
                                    key="lõuend")],
                                    [sg.Text('Vastuseid A oli -'), sg.Text(str(valik_A))],
                                    [sg.Text('Vastuseid B oli -'), sg.Text(str(valik_B))],
                                    [sg.Cancel('Välju')]]
                                
                                aken = sg.Window("SÕBRAD!", paigutus6)
                                aken.Finalize()
                                minu_lõuend = aken.Element("lõuend")
                                taustapilt = minu_lõuend.DrawImage(filename="tulemus4.png", location=(0, 0))
                                
                                syndmus6, v22rtused6 = aken.read()
                                
                                if syndmus6 == "Välju" or syndmus6 == sg.WIN_CLOSED:
                                    aken.close()
                                    break
                                    
                                    
                            
                                    
                                    
                            if str(valik_A) > str(valik_B):
                                paigutus7 = [[sg.Graph(
                                    canvas_size =(800, 600),
                                    graph_bottom_left=(0, 800),
                                    graph_top_right=(800, 0),
                                    key="lõuend")],
                                    [sg.Text('Vastuseid A oli -'), sg.Text(str(valik_A))],
                                    [sg.Text('Vastuseid B oli -'), sg.Text(str(valik_B))],
                                    [sg.Cancel('Välju')]]
                                
                                aken = sg.Window("SÕBRAD!", paigutus7)
                                aken.Finalize()
                                minu_lõuend = aken.Element("lõuend")
                                taustapilt = minu_lõuend.DrawImage(filename="tulemus3.png", location=(0, 0))
                                
                                syndmus7, v22rtused7 = aken.read()

                                if syndmus7 == "Välju" or syndmus7 == sg.WIN_CLOSED:
                                    aken.close()
                                    break
                                aken.close()
                            
        if syndmus01 == "Suhted":
            aken.close()
            
           
           
            paigutus1 = [[sg.Graph(
                canvas_size =(800, 600),
                graph_bottom_left=(0, 800),
                graph_top_right=(800, 0),
                key="lõuend")],
                [sg.Text('SUHTED')],
                [sg.Text('Su kaaslane näeb, et sa oled juba 15 minutit kellegagi kirjutanud.')],
                [sg.Text('Kuidas ta sellele reageerib?')],
                [sg.Button('A'), sg.Text('A: Laseb sul rahulikult edasi suhelda.')],
                [sg.Button('B'), sg.Text('B: Krabab su telefoni ja hakkab nuhkima.')],
                [sg.Cancel('Välju')]]
        
            aken = sg.Window("SUHTED!", paigutus1)
            aken.Finalize()
            minu_lõuend = aken.Element("lõuend")
            taustapilt = minu_lõuend.DrawImage(filename="taustsuhe.png", location=(0, 0))
            
        
            syndmus1, v22rtused1 = aken.Read()

            # sulge programm, kui vajutatakse Välju või suletakse aken X-st
            if syndmus1 == "Välju" or syndmus1 == sg.WIN_CLOSED:
                aken.close()
                break
            if syndmus1 == "A" or syndmus1 == "B":
                aken.close()

                if syndmus1 == "A":
                    valik_A += 1
                if syndmus1 == "B":
                    valik_B += 1
                
                # loome akna uue järjendiga
                paigutus2 = [[sg.Graph(
                    canvas_size =(800, 600),
                    graph_bottom_left=(0, 800),
                    graph_top_right=(800, 0),
                    key="lõuend")],
                    [sg.Text('Sa lähed oma vana sõbraga välja, aga unustad oma kaaslasele öelda, et jääd kauemaks kui plaanitud.')],
                    [sg.Text('Mida teeb su kaaslane kui sa planeeritud ajaks koju pole jõudnud?')],
                    [sg.Button('A'), sg.Text('Kirjutab sulle ja uurib kas kõik on korras?')],
                    [sg.Button('B'), sg.Text('Otsib su linna pealt üles ja vihastab.')],
                    [sg.Cancel('Välju')]]
                
                aken = sg.Window("SUHTED!", paigutus2)
                aken.Finalize()
                minu_lõuend = aken.Element("lõuend")
                taustapilt = minu_lõuend.DrawImage(filename="taustsuhe.png", location=(0, 0))
                
                syndmus2, v22rtused2 = aken.read()

                if syndmus2 == "Välju" or syndmus2 == sg.WIN_CLOSED:
                    aken.close()
                    break
                if syndmus2 == "A" or syndmus2 == "B":
                    aken.close()

                    if syndmus2 == "A":
                        valik_A += 1
                    if syndmus2 == "B":
                        valik_B += 1

                    # loome akna uue järjendiga
                    paigutus3 = [[sg.Graph(
                        canvas_size =(800, 600),
                        graph_bottom_left=(0, 800),
                        graph_top_right=(800, 0),
                        key="lõuend")],
                        [sg.Text('Kuidas sa tunned ennast oma kaaslase juuresolekul?')],
                        [sg.Button('A'), sg.Text('Sa oled rõõmus ja saad olla sina ise.')],
                        [sg.Button('B'), sg.Text('Sa oled stressis ja kardad vigu teha.')],
                        [sg.Cancel('Välju')]]
                    
                    aken = sg.Window("SUHTED!", paigutus3)
                    aken.Finalize()
                    minu_lõuend = aken.Element("lõuend")
                    taustapilt = minu_lõuend.DrawImage(filename="taustsuhe.png", location=(0, 0))
                    
                    syndmus3, v22rtused3 = aken.read()

                    if syndmus3 == "Välju" or syndmus3 == sg.WIN_CLOSED:
                        aken.close()
                        break
                    if syndmus3 == "A" or syndmus3 == "B":
                        aken.close()

                        if syndmus3 == "A":
                            valik_A += 1
                        if syndmus3 == "B":
                            valik_B += 1

                        # loome akna uue järjendiga
                        paigutus4 = [[sg.Graph(
                            canvas_size =(800, 600),
                            graph_bottom_left=(0, 800),
                            graph_top_right=(800, 0),
                            key="lõuend")],
                            [sg.Text('Su kaaslane ütleb, et ta läheb tööle, aga pärast kuuled ta sõbralt, et nad olid hoopis koos väljas.')],
                            [sg.Text('Kuidas reageerib su kaaslane kui sa talle sellest räägid?')],
                            [sg.Button('A'), sg.Text('Vabandab, et ta unustas sulle teatada, et ta plaanid muutusid.')],
                            [sg.Button('B'), sg.Text('Saab pahaseks, et sa teda valetamises süüdistad.')],
                            [sg.Cancel('Välju')]]
                        
                        aken = sg.Window("SUHTED!", paigutus4)
                        aken.Finalize()
                        minu_lõuend = aken.Element("lõuend")
                        taustapilt = minu_lõuend.DrawImage(filename="taustsuhe.png", location=(0, 0))
                        
                        syndmus4, v22rtused4 = aken.read()

                        if syndmus4 == "Välju" or syndmus4 == sg.WIN_CLOSED:
                            aken.close()
                            break
                        if syndmus4 == "A" or syndmus4 == "B":
                            aken.close()

                            if syndmus4 == "A":
                                valik_A += 1
                            if syndmus4 == "B":
                                valik_B += 1

                            # loome akna uue järjendiga
                            paigutus5 = [[sg.Graph(
                                canvas_size =(800, 600),
                                graph_bottom_left=(0, 800),
                                graph_top_right=(800, 0),
                                key="lõuend")],
                                [sg.Text('Sa oled haige ja palud oma kaaslasel ennast arsti juurde sõidutada.')],
                                [sg.Text('Kuidas ta sellele vastab?')],
                                [sg.Button('A'), sg.Text('Muidugi ma sõidutan sind! Sa oled mind ju samamoodi aidanud.')],
                                [sg.Button('B'), sg.Text('Ma ei viitsi sind ringi sõidutada. Mine bussiga või midagi.')],
                                [sg.Cancel('Välju')]]
                            
                            aken = sg.Window("SUHTED!", paigutus5)
                            aken.Finalize()
                            minu_lõuend = aken.Element("lõuend")
                            taustapilt = minu_lõuend.DrawImage(filename="taustsuhe.png", location=(0, 0))
                            
                            syndmus5, v22rtused5 = aken.read()

                            if syndmus5 == "Välju" or syndmus5 == sg.WIN_CLOSED:
                                aken.close()
                                break
                            if syndmus5 == "A" or syndmus5 == "B":
                                aken.close()

                                if syndmus5 == "A":
                                    valik_A += 1
                                if syndmus5 == "B":
                                    valik_B += 1
                            
                            
                            if str(valik_A) < str(valik_B):
                                paigutus6 = [[sg.Graph(
                                    canvas_size =(800, 600),
                                    graph_bottom_left=(0, 800),
                                    graph_top_right=(800, 0),
                                    key="lõuend")],
                                    [sg.Text('Vastuseid A oli -'), sg.Text(str(valik_A))],
                                    [sg.Text('Vastuseid B oli -'), sg.Text(str(valik_B))],
                                    [sg.Cancel('Välju')]]
                                
                                aken = sg.Window("SUHTED!", paigutus6)
                                aken.Finalize()
                                minu_lõuend = aken.Element("lõuend")
                                taustapilt = minu_lõuend.DrawImage(filename="tulemus2.png", location=(0, 0))
                                
                                syndmus6, v22rtused6 = aken.read()

                                if syndmus6 == "Välju" or syndmus6 == sg.WIN_CLOSED:
                                    aken.close()
                                    break
                            
                                    
                                    
                            if str(valik_A) > str(valik_B):
                                paigutus7 = [[sg.Graph(
                                    canvas_size =(800, 600),
                                    graph_bottom_left=(0, 800),
                                    graph_top_right=(800, 0),
                                    key="lõuend")],
                                    [sg.Text('Vastuseid A oli -'), sg.Text(str(valik_A))],
                                    [sg.Text('Vastuseid B oli -'), sg.Text(str(valik_B))],
                                    [sg.Cancel('Välju')]]
                                
                                aken = sg.Window("SUHTED!", paigutus7)
                                aken.Finalize()
                                minu_lõuend = aken.Element("lõuend")
                                taustapilt = minu_lõuend.DrawImage(filename="tulemus1.png", location=(0, 0))
                                
                                syndmus7, v22rtused7 = aken.read()

                                if syndmus7 == "Välju" or syndmus7 == sg.WIN_CLOSED:
                                    aken.close()
                                    break
                                aken.close()
                                
                                                   
            
        if syndmus01 == "Sina":
            aken.close()
            
           
           
            paigutus1 = [[sg.Graph(
                canvas_size =(800, 600),
                graph_bottom_left=(0, 800),
                graph_top_right=(800, 0),
                key="lõuend")],
                [sg.Text('SINA')],
                [sg.Text('Sa helistad oma sõbrale, aga ta ei võta vastu ega helista sulle päeva jooksul tagasi.')],
                [sg.Text('Kuidas sa reageerid?')],
                [sg.Button('A'), sg.Text('A: Ma ei hakka üle mõtlema. Ilmselt oli tal täna kiire päev.')],
                [sg.Button('B'), sg.Text('B: Miks ta ei helista? Kas ma tegin midagi valesti?! Kas ta vihkab mind?! Kas temaga juhtus midagi? APPI!')],
                [sg.Cancel('Välju')]]
        
            aken = sg.Window("SINA!", paigutus1)
            aken.Finalize()
            minu_lõuend = aken.Element("lõuend")
            taustapilt = minu_lõuend.DrawImage(filename="sina.png", location=(0, 0))
            
        
            syndmus1, v22rtused1 = aken.Read()

            # sulge programm, kui vajutatakse Välju või suletakse aken X-st
            if syndmus1 == "Välju" or syndmus1 == sg.WIN_CLOSED:
                aken.close()
                break
            if syndmus1 == "A" or syndmus1 == "B":
                aken.close()

                if syndmus1 == "A":
                    valik_A += 1
                if syndmus1 == "B":
                    valik_B += 1
                
                # loome akna uue järjendiga
                paigutus2 = [[sg.Graph(
                    canvas_size =(800, 600),
                    graph_bottom_left=(0, 800),
                    graph_top_right=(800, 0),
                    key="lõuend")],
                    [sg.Text('Sa kõnnid tänaval ja komistad.')],
                    [sg.Text('Mida sa teed?')],
                    [sg.Button('A'), sg.Text('Kõnnid rahulikult edasi ja unustad komistuse?')],
                    [sg.Button('B'), sg.Text('Mõtled kogu päeva sellele kui piinlik sul oli ja arvad, et kõik nägid ja naersid salaja su üle.')],
                    [sg.Cancel('Välju')]]
                
                aken = sg.Window("SINA!", paigutus2)
                aken.Finalize()
                minu_lõuend = aken.Element("lõuend")
                taustapilt = minu_lõuend.DrawImage(filename="sina.png", location=(0, 0))
                
                syndmus2, v22rtused2 = aken.read()

                if syndmus2 == "Välju" or syndmus2 == sg.WIN_CLOSED:
                    aken.close()
                    break
                if syndmus2 == "A" or syndmus2 == "B":
                    aken.close()

                    if syndmus2 == "A":
                        valik_A += 1
                    if syndmus2 == "B":
                        valik_B += 1

                    # loome akna uue järjendiga
                    paigutus3 = [[sg.Graph(
                        canvas_size =(800, 600),
                        graph_bottom_left=(0, 800),
                        graph_top_right=(800, 0),
                        key="lõuend")],
                        [sg.Text('Sa saad koolis halva hinde.')],
                        [sg.Text('Kuidas sa reageerid')],
                        [sg.Button('A'), sg.Text('Nojah see töö läks halvasti, aga küll ma järgmine kord paremini teen.')],
                        [sg.Button('B'), sg.Text('Kuidas ma seda ei osanud? Miks ma üldse siin koolis käin?! Ma ei saa millegagi hakkama!')],
                        [sg.Cancel('Välju')]]
                    
                    aken = sg.Window("SINA!", paigutus3)
                    aken.Finalize()
                    minu_lõuend = aken.Element("lõuend")
                    taustapilt = minu_lõuend.DrawImage(filename="sina.png", location=(0, 0))
                    
                    syndmus3, v22rtused3 = aken.read()

                    if syndmus3 == "Välju" or syndmus3 == sg.WIN_CLOSED:
                        aken.close()
                        break
                    if syndmus3 == "A" or syndmus3 == "B":
                        aken.close()

                        if syndmus3 == "A":
                            valik_A += 1
                        if syndmus3 == "B":
                            valik_B += 1

                        # loome akna uue järjendiga
                        paigutus4 = [[sg.Graph(
                            canvas_size =(800, 600),
                            graph_bottom_left=(0, 800),
                            graph_top_right=(800, 0),
                            key="lõuend")],
                            [sg.Text('Millele sa enda puhul rohkem keskendud?')],
                            [sg.Button('A'), sg.Text('Positiivsele.')],
                            [sg.Button('B'), sg.Text('Negatiivsele')],
                            [sg.Cancel('Välju')]]
                        
                        aken = sg.Window("SINA!", paigutus4)
                        aken.Finalize()
                        minu_lõuend = aken.Element("lõuend")
                        taustapilt = minu_lõuend.DrawImage(filename="sina.png", location=(0, 0))
                        
                        syndmus4, v22rtused4 = aken.read()

                        if syndmus4 == "Välju" or syndmus4 == sg.WIN_CLOSED:
                            aken.close()
                            break
                        if syndmus4 == "A" or syndmus4 == "B":
                            aken.close()

                            if syndmus4 == "A":
                                valik_A += 1
                            if syndmus4 == "B":
                                valik_B += 1

                            # loome akna uue järjendiga
                            paigutus5 = [[sg.Graph(
                                canvas_size =(800, 600),
                                graph_bottom_left=(0, 800),
                                graph_top_right=(800, 0),
                                key="lõuend")],
                                [sg.Text('Sul on probleem ja mõtled kas sellest oma sõbrale rääkida või mitte.')],
                                [sg.Text('Mida sa teed?')],
                                [sg.Button('A'), sg.Text('Räägid oma sõbrale, sest äkki ta oskab sind aidata.')],
                                [sg.Button('B'), sg.Text('Jätad enda teada, sest sa ei taha olla koormaks oma mõttetute probleemidega.')],
                                [sg.Cancel('Välju')]]
                            
                            aken = sg.Window("SINA!", paigutus5)
                            aken.Finalize()
                            minu_lõuend = aken.Element("lõuend")
                            taustapilt = minu_lõuend.DrawImage(filename="sina.png", location=(0, 0))
                            
                            syndmus5, v22rtused5 = aken.read()

                            if syndmus5 == "Välju" or syndmus5 == sg.WIN_CLOSED:
                                aken.close()
                                break
                            if syndmus5 == "A" or syndmus5 == "B":
                                aken.close()

                                if syndmus5 == "A":
                                    valik_A += 1
                                if syndmus5 == "B":
                                    valik_B += 1
                            
                            
                            if str(valik_A) < str(valik_B):
                                paigutus6 = [[sg.Graph(
                                    canvas_size =(800, 600),
                                    graph_bottom_left=(0, 800),
                                    graph_top_right=(800, 0),
                                    key="lõuend")],
                                    [sg.Text('Vastuseid A oli -'), sg.Text(str(valik_A))],
                                    [sg.Text('Vastuseid B oli -'), sg.Text(str(valik_B))],
                                    [sg.Cancel('Välju')]]
                                
                                aken = sg.Window("SINA!", paigutus6)
                                aken.Finalize()
                                minu_lõuend = aken.Element("lõuend")
                                taustapilt = minu_lõuend.DrawImage(filename="tulemus6.png", location=(0, 0))
                                
                                syndmus6, v22rtused6 = aken.read()

                                if syndmus6 == "Välju" or syndmus6 == sg.WIN_CLOSED:
                                    aken.close()
                                    break
                            
                                    
                                    
                            if str(valik_A) > str(valik_B):
                                paigutus7 = [[sg.Graph(
                                    canvas_size =(800, 600),
                                    graph_bottom_left=(0, 800),
                                    graph_top_right=(800, 0),
                                    key="lõuend")],
                                    [sg.Text('Vastuseid A oli -'), sg.Text(str(valik_A))],
                                    [sg.Text('Vastuseid B oli -'), sg.Text(str(valik_B))],
                                    [sg.Cancel('Välju')]]
                                
                                aken = sg.Window("SINA!", paigutus7)
                                aken.Finalize()
                                minu_lõuend = aken.Element("lõuend")
                                taustapilt = minu_lõuend.DrawImage(filename="tulemus5.png", location=(0, 0))
                                
                                syndmus7, v22rtused7 = aken.read()

                                if syndmus7 == "Välju" or syndmus7 == sg.WIN_CLOSED:
                                    aken.close()
                                break
                            aken.close()
                            
        
