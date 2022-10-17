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


aken = sg.Window("Joonistame!", paigutus0)
aken.Finalize()
minu_lõuend = aken.Element("lõuend")
start = minu_lõuend.DrawImage(filename="start.png", location=(0, 0))
#taustapilt = minu_lõuend.DrawImage(filename="taustsober.png", location=(0, 0))

# loome tegevused
while True:
    syndmus0, v22rtused0 = aken.Read()

    # sulge programm, kui vajutatakse Välju või suletakse aken X-st
    if syndmus0 == "Välju" or syndmus0 == sg.WIN_CLOSED:
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
    
        aken = sg.Window("Joonistame!", paigutus01)
        aken.Finalize()
        minu_lõuend = aken.Element("lõuend")
        taustapilt = minu_lõuend.DrawImage(filename="valik1.png", location=(0, 0))
        
    
    syndmus01, v22rtused01 = aken.Read()
    
    if syndmus01 == "Välju" or syndmus01 == sg.WIN_CLOSED:
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
    
        aken = sg.Window("Joonistame!", paigutus1)
        aken.Finalize()
        minu_lõuend = aken.Element("lõuend")
        taustapilt = minu_lõuend.DrawImage(filename="taustsober.png", location=(0, 0))
        
    
    syndmus1, v22rtused1 = aken.Read()

    # sulge programm, kui vajutatakse Välju või suletakse aken X-st
    if syndmus1 == "Välju" or syndmus1 == sg.WIN_CLOSED:
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
        
        aken = sg.Window("Joonistame!", paigutus2)
        aken.Finalize()
        minu_lõuend = aken.Element("lõuend")
        taustapilt = minu_lõuend.DrawImage(filename="taustsober.png", location=(0, 0))
        
        syndmus2, v22rtused2 = aken.read()

        if syndmus2 == "Välju" or syndmus2 == sg.WIN_CLOSED:
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
            
            aken = sg.Window("Joonistame!", paigutus3)
            aken.Finalize()
            minu_lõuend = aken.Element("lõuend")
            taustapilt = minu_lõuend.DrawImage(filename="taustsober.png", location=(0, 0))
            
            syndmus3, v22rtused3 = aken.read()

            if syndmus3 == "Välju" or syndmus3 == sg.WIN_CLOSED:
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
                
                aken = sg.Window("Joonistame!", paigutus4)
                aken.Finalize()
                minu_lõuend = aken.Element("lõuend")
                taustapilt = minu_lõuend.DrawImage(filename="taustsober.png", location=(0, 0))
                
                syndmus4, v22rtused4 = aken.read()

                if syndmus4 == "Välju" or syndmus4 == sg.WIN_CLOSED:
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
                    
                    aken = sg.Window("Joonistame!", paigutus5)
                    aken.Finalize()
                    minu_lõuend = aken.Element("lõuend")
                    taustapilt = minu_lõuend.DrawImage(filename="taustsober.png", location=(0, 0))
                    
                    syndmus5, v22rtused5 = aken.read()

                    if syndmus5 == "Välju" or syndmus5 == sg.WIN_CLOSED:
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
                            [sg.Text('Sinu sõber on halb')],
                            [sg.Text('Vastuseid A oli -'), sg.Text(str(valik_A))],
                            [sg.Text('Vastuseid B oli -'), sg.Text(str(valik_B))],
                            [sg.Cancel('Välju')]]
                        
                        aken = sg.Window("Joonistame!", paigutus6)
                        aken.Finalize()
                        minu_lõuend = aken.Element("lõuend")
                        taustapilt = minu_lõuend.DrawImage(filename="taustsober.png", location=(0, 0))
                        
                        syndmus6, v22rtused6 = aken.read()

                        if syndmus6 == "Välju" or syndmus6 == sg.WIN_CLOSED:
                            break
                    
                            
                            
                    if str(valik_A) > str(valik_B):
                        paigutus7 = [[sg.Graph(
                            canvas_size =(800, 600),
                            graph_bottom_left=(0, 800),
                            graph_top_right=(800, 0),
                            key="lõuend")],
                            [sg.Text('Sinu sõber on hea')],
                            [sg.Text('Vastuseid A oli -'), sg.Text(str(valik_A))],
                            [sg.Text('Vastuseid B oli -'), sg.Text(str(valik_B))],
                            [sg.Cancel('Välju')]]
                        
                        aken = sg.Window("Joonistame!", paigutus7)
                        aken.Finalize()
                        minu_lõuend = aken.Element("lõuend")
                        taustapilt = minu_lõuend.DrawImage(filename="taustsober.png", location=(0, 0))
                        
                        syndmus7, v22rtused7 = aken.read()

                        if syndmus7 == "Välju" or syndmus7 == sg.WIN_CLOSED:
                            break
                        
                        

                        # loome akna uue järjendiga
#                         paigutus6 = [[sg.Graph(
#                             canvas_size =(800, 600),
#                             graph_bottom_left=(0, 800),
#                             graph_top_right=(800, 0),
#                             key="lõuend")],
#                             [sg.Text('Tulemused:')],
#                             [sg.Text('Vastuseid A oli -'), sg.Text(str(valik_A))],
#                             [sg.Text('Vastuseid B oli -'), sg.Text(str(valik_B))],
#                             [sg.Cancel('Välju')]]
#                         
#                         aken = sg.Window("Joonistame!", paigutus6)
#                         aken.Finalize()
#                         minu_lõuend = aken.Element("lõuend")
#                         taustapilt = minu_lõuend.DrawImage(filename="taustsober.png", location=(0, 0))
#                         
#                         syndmus6, v22rtused6 = aken.read()
# 
#                         if syndmus6 == "Välju" or syndmus6 == sg.WIN_CLOSED:
#                             break


aken.close()
