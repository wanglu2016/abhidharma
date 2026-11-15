# Concept atlas for the site.
# Terms follow the author's 《俱舍》術語要點一覽 (《俱舍九題》 pp. 14-17).
# tier (from the author's own 要點 paragraph): key=要點/根本/核心, hard=難點, method=基本操作, term=術語舉要所列.
# memo=True: listed in the author's entrance test (默寫九十八隨眠、七十五法、三十七道品、二十二根).
# wzq: verbatim paragraphs from 《俱舍萬字》 as (section, first, last) — 0-based, inclusive.
# zh/en: editor's short definitions, used where 《萬字》 does not cover the term.
# aq: the author's own remark (from 《俱舍九題》 「要點」), with English rendering aq_en.
# verse: substrings located in the CBETA T1560 verses; jt: 九題 numbers; bx: 英譯百瑕 entry numbers.

PINS = [
    # id, name (trad), simplified, English, juan, verses (by four-line count), author's assessment
    ("jie", "分別界品", "分别界品", "Dhātu: the elements", "1–2", 44),
    ("gen", "分別根品", "分别根品", "Indriya: the faculties", "3–7", 74),
    ("shi", "分別世間品", "分别世间品", "Loka: the world", "8–12", 99),
    ("ye", "分別業品", "分别业品", "Karma: action", "13–18", 131),
    ("sui", "分別隨眠品", "分别随眠品", "Anuśaya: latent defilements", "19–21", 69),
    ("xian", "分別賢聖品", "分别贤圣品", "Pudgala-mārga: persons and the path", "22–25", 83),
    ("zhi", "分別智品", "分别智品", "Jñāna: knowledge", "26–27", 61),
    ("ding", "分別定品", "分别定品", "Samāpatti: meditative attainment", "28–29", 39),
    ("po", "破執我品", "破执我品", "Refutation of the self", "29–30", 0),
]

# The author's assessment of each chapter (《俱舍九題》「要點」), verbatim, with English.
PIN_NOTES = {
    "jie": ("「蘊處界」是要點。「四諦」和「有漏無漏」的分別是根本。「有尋有伺等」四料簡是基本操作。四料簡會出現在阿毘達磨的幾乎一切地方。總體上，界品比較基礎，沒有獨立的難點。",
            "The aggregates, sense-bases and elements are the key points. The four truths and the distinction of with-outflow and outflow-free are fundamental. The fourfold sorting of 'with vitarka and vicāra' etc. is a basic operation, and fourfold sorting appears almost everywhere in Abhidharma. On the whole this chapter is foundational and has no difficulty of its own."),
    "gen": ("「二十二根」是要點。分別異熟、三性、見所斷等，是基本操作。這些奠定了阿毘達磨的基本方法。六因四緣五果是難點。十二或二十心的無間相生問題，如果搞清楚，阿毘達磨算入門了，就可以大致看懂《識身》，否則《識身》就是天書。",
            "The twenty-two faculties are the key point. Analysing them as retribution, by the three natures, by mode of abandonment and so on is a basic operation; this lays down the basic method of Abhidharma. The six causes, four conditions and five fruits are the difficult point. Once the immediate succession of the twelve (or twenty) minds is clear, you have entered Abhidharma and can roughly follow the Vijñānakāya; otherwise that text is unreadable."),
    "shi": ("這一品比較次要。學阿毘達磨千萬不要把時間耗在畫世界圖上。說白了，那些只是一個頌：「四大洲日月」。不過，本品埋藏一些對理解其他部分稍有幫助的細節，尤其是「中有」。",
            "This chapter is relatively secondary. Never spend your time drawing maps of the cosmos; all that is really one verse, 'the four continents, sun and moon'. Still, the chapter hides some details that help with other parts, above all the intermediate existence."),
    "ye": ("這是篇幅最長的一品。要點是三種律儀、律儀的得捨。無表需要注意。沒有獨立的難點，但細節繁多。「捨定生善法」、「捨聖由得果」兩頌尤其重要。",
            "The longest chapter. The key points are the three restraints and how restraint is obtained and relinquished. Non-informative matter needs attention. No difficulty of its own, but many details. The two verses beginning 'relinquishing good dharmas born of meditation' and 'relinquishing the noble [restraint] by attaining a fruit' are especially important."),
    "sui": ("這是重要的一品，也是最難的一品。要搞清楚「隨眠隨增」。根品中「十二或二十心等無間相生」的問題搞清楚，阿毘達磨算登堂了；隨眠品中「諸根緣緣識各有幾隨眠隨增」的問題搞清楚，阿毘達磨算入室了。一旦入室，看《品類》不會有太大難度。能無障礙閱讀《品類》，你就是阿毘達磨專家。",
            "An important chapter, and the hardest. You must get clear how anuśayas adhere-and-grow. Clear up the immediate succession of the twelve or twenty minds in the faculties chapter and you have reached the hall; clear up how many anuśayas adhere-and-grow in the consciousness cognizing [the consciousness cognizing] each faculty, and you have entered the inner room. After that the Prakaraṇa is not very hard; read the Prakaraṇa without obstruction and you are an Abhidharma expert."),
    "xian": ("這是最有意思的一品。從四念住到阿羅漢果，值得常常涵泳。四果和九遍知的安立，和定品、隨眠品關係密切。隨眠品、賢聖品、定品，這三品是分不開的。如果《俱舍》只有時間學三品，一定是這三品。這三品學好，界品、根品自然就理解深入了。",
            "The most interesting chapter: from the applications of mindfulness to arhatship it rewards constant immersion. How the four fruits and the nine thorough knowledges are established is closely tied to the meditation and anuśaya chapters. These three chapters cannot be separated. If you only have time for three chapters of the Kośa, they must be these three; learn them well and your understanding of the first two chapters deepens by itself."),
    "zhi": ("這一品主要是應用。對初學者來說，不用過早關心。跳過對其他品影響不大。而一旦你打牢基礎之後，目光轉向「得修」，就從陸地進入了大海，足以領略阿毘達磨的壯闊。要點是「十智」和「六通」，難點是「得修」。",
            "Mainly application. Beginners need not worry about it early; skipping it hardly affects the other chapters. But once your foundation is firm and you turn to 'cultivation by acquisition', you move from land into the ocean and see the full grandeur of Abhidharma. Key points: the ten knowledges and six supernormal powers; the difficult point: cultivation by acquisition."),
    "ding": ("這一品可以最先學。禪支等是比較有意思的。定靜慮比生靜慮對理解阿毘達磨更重要。阿毘達磨的核心就是兩個字：離染。",
             "This chapter can be learned first. The dhyāna factors and the like are rather interesting. The dhyānas as meditative attainment matter more for understanding Abhidharma than the dhyānas as places of rebirth. The core of Abhidharma is one word: detachment (離染)."),
    "po": ("（作者〈術語舉要〉未列本品術語。）", "(The author's term list does not cover this chapter.)"),
}

# Gloss of Puguang's structure (光記 T41, 1c16–2a19)
STRUCTURE = {
    "jie": ("總明", "諸法體"), "gen": ("總明", "諸法用"),
    "shi": ("別明有漏", "果"), "ye": ("別明有漏", "因"), "sui": ("別明有漏", "緣"),
    "xian": ("別明無漏", "果"), "zhi": ("別明無漏", "因"), "ding": ("別明無漏", "緣"),
    "po": ("釋無我理", ""),
}

READING_ORDER = [["ding"], ["xian", "sui"], ["jie", "gen"], ["ye"], ["shi", "zhi"]]

C = []
def add(**k): C.append(k)

# ───────────── 界品 ─────────────
add(id="youlou", pin="jie", t="有漏・無漏", skt="sāsrava · anāsrava", en="with-outflow · outflow-free",
    tier="key", wzq=[("1.1", 3, 5), ("1.1", 13, 15)],
    note_zh="「有漏」不等於「染污」：有隨眠心有「有染」「無染」兩類，無染有漏心亦是有漏。英文 contaminated、defiled 一類譯法容易引起這種混淆（見《英譯百瑕》序）。",
    note_en="Sāsrava does not mean 'defiled': minds with anuśaya are either defiled or undefiled, and an undefiled sāsrava mind is still sāsrava. Renderings such as 'contaminated' invite this confusion (see the preface to the 100 Flaws).",
    verse=["於彼漏隨增", "無漏謂道諦"], rel=["suizeng", "sidi", "sanwuwei", "yousuimianxin"])
add(id="sidi", pin="jie", t="四諦", skt="catvāri āryasatyāni", en="the four noble truths",
    tier="key", wzq=[("1.1", 8, 12), ("1.1", 17, 17)],
    verse=["有漏名取蘊"], rel=["youlou", "shiliu", "sanwuwei", "jiandao"])
add(id="sanwuwei", pin="jie", t="三無為", skt="trividham asaṃskṛtam", en="the three unconditioned",
    tier="term", wzq=[("1.1", 0, 2), ("1.1", 16, 16)],
    verse=["擇滅謂離繫", "畢竟礙當生"], rel=["youlou", "sixiang", "de"])
add(id="wuyun", pin="jie", t="五蘊", skt="pañca skandhāḥ", en="the five aggregates",
    tier="key", wzq=[("1.2", 0, 0), ("1.2", 3, 3), ("1.2", 6, 10), ("1.2", 12, 12)],
    verse=["又諸有為法", "色者唯五根"], jt=[2], rel=["shierchu", "shibajie", "qishiwu", "biaowubiao"])
add(id="shierchu", pin="jie", t="十二處", skt="dvādaśa āyatanāni", en="the twelve sense-bases",
    tier="key", wzq=[("1.2", 1, 1), ("1.2", 4, 4), ("1.2", 13, 13)],
    verse=["四餘名行蘊"], jt=[2], rel=["wuyun", "shibajie", "neiwai"])
add(id="shibajie", pin="jie", t="十八界", skt="aṣṭādaśa dhātavaḥ", en="the eighteen elements",
    tier="key", wzq=[("1.2", 2, 2), ("1.2", 5, 5), ("1.2", 14, 15)],
    note_zh="界品後半以有見、有對、三性、三界繫、有漏、尋伺、有所緣、執受等諸門分別十八界，是阿毘達磨「分別」方法的第一次系統操練。",
    note_en="The second half of the chapter analyses the eighteen elements by gate after gate (visible, resistant, three natures, realm, with-outflow, vitarka-vicāra, having an object, appropriated…): the first systematic exercise of Abhidharma's method of analysis (vibhaṅga).",
    verse=["識謂各了別", "一有見謂色"], jt=[2], rel=["wuyun", "shierchu", "zhishou", "neiwai", "xunsi"])
add(id="qishiwu", pin="jie", t="七十五法", skt="pañca vastūni", en="the seventy-five dharmas in five groups",
    tier="term", memo=True, wzq=[("1.3", 0, 8)], jt=[6], rel=["xinsuo", "buxiangying", "wuyun", "sanwuwei"])
add(id="xunsi", pin="jie", t="有尋有伺等（三地）", skt="savitarka-savicāra etc.", en="with vitarka and vicāra, etc. (the three stages)",
    tier="method", wzq=[("2.1", 8, 11)],
    zh_extra="界品頌：「五識唯尋伺，後三三餘無。」",
    en_extra="Verse in the Dhātu chapter: 'The five consciousnesses are only with vitarka and vicāra; the last three [elements] are of all three kinds; the rest are without.'",
    verse=["五識唯尋伺"], rel=["shibajie", "sanjie", "zhongjinglv", "chanzhi"])
add(id="sanfenbie", pin="jie", t="三分別", skt="trividha vikalpa", en="the three kinds of discrimination",
    tier="term",
    zh_def="自性分別、計度分別、隨念分別。五識有自性分別（以尋為體），而無計度、隨念二分別，故說五識「無分別」。計度分別以意地散慧為體，隨念分別以意地諸念為體。",
    en_def="Discrimination by intrinsic nature, by conceptual construction, and by recollection. The five sense consciousnesses have discrimination by intrinsic nature (whose substance is vitarka) but lack the other two, so they are said to be 'without discrimination'. Conceptual construction is the non-meditative understanding of the mental stage; recollection is the mindfulness of the mental stage.",
    verse=["說五無分別"], rel=["xunsi", "shibajie"])
add(id="zhishou", pin="jie", t="執受", skt="upātta", en="appropriated",
    tier="term",
    zh_def="心心所法共所執持、攝為依處者，名有執受（如現在身中的五根及不離根的色香味觸）。頌曰：「前八界及聲，無執受餘二。」七心界、法界、聲界九界唯無執受，餘九界通二。",
    en_def="What mind and mental factors jointly hold and take as their support is 'appropriated' (e.g. the present sense faculties and the visible form, odour, taste and tangibles inseparable from them). The seven mind-elements, the dharma element and sound — nine elements — are never appropriated; the other nine may be either.",
    note_zh="法界是「全」無執受，不是「一半」。", note_en="The dharma element is wholly non-appropriated, not 'one half' of it.",
    verse=["七心法界半"], bx=[1], rel=["shibajie"])
add(id="neiwai", pin="jie", t="內外", skt="ādhyātmika · bāhya", en="internal and external",
    tier="term",
    zh_def="頌曰：「內十二眼等，色等六為外。」十八界中，六根、六識十二界為內，色等六境為外。",
    en_def="Of the eighteen elements, the six faculties and six consciousnesses (twelve) are internal; the six objects beginning with visible form are external.",
    verse=["內十二眼等"], rel=["shibajie", "shierchu"])

# ───────────── 根品 ─────────────
add(id="ershier", pin="gen", t="二十二根", skt="dvāviṃśatir indriyāṇi", en="the twenty-two faculties",
    tier="key", memo=True, wzq=[("2.3", 0, 5)],
    verse=["見修無學道"], jt=[5, 6, 7], bx=[3, 6], rel=["yishu", "sanxing", "jiansuoduan", "xinsuo"])
add(id="yishu", pin="gen", t="異熟・有異熟", skt="vipāka · savipāka", en="retribution · having retribution",
    tier="method", wzq=[("2.3", 7, 8)],
    zh_extra="異熟是異熟因所生果，性唯無覆無記；有異熟指能招異熟者，即有漏善與不善。",
    en_extra="A retribution (vipāka) is the fruit of a retribution cause and is always unobscured-indeterminate; 'having retribution' (savipāka) means able to produce one, i.e. with-outflow wholesome and unwholesome dharmas.",
    note_zh="「生得善」不是異熟，異熟唯無記。", note_en="Innate wholesome (upapattilābhika) is not retribution: retribution is only indeterminate.",
    verse=["命唯是異熟", "憂定有異熟"], bx=[100], rel=["ershier", "liuyin", "wuguo", "sanxing"])
add(id="sanxing", pin="gen", t="三性", skt="kuśala · akuśala · avyākṛta", en="the three natures: wholesome, unwholesome, indeterminate",
    tier="method", wzq=[("2.4", 2, 3), ("2.3", 6, 6)],
    zh_extra="無記分有覆、無覆。有覆無記是染污而非不善，如色無色界煩惱，以及欲界身見、邊見與彼相應痴。",
    en_extra="The indeterminate is obscured or unobscured. Obscured-indeterminate dharmas are defiled but not unwholesome, e.g. the defilements of the higher realms, and the self-view and extreme view of the sensuous realm with the delusion associated with them.",
    verse=["唯善後八根", "勝義善解脫"], jt=[1], bx=[8, 100], rel=["ershier", "yishu", "shierxin"])
add(id="jiansuoduan", pin="gen", t="見所斷等（三界十五部）", skt="darśanaheya · bhāvanāheya · aheya", en="abandoned by seeing, by cultivation, not to be abandoned",
    tier="method", wzq=[("2.1", 2, 5), ("2.1", 13, 14), ("2.3", 9, 9)],
    verse=["意三受通三", "不染非六生"], jt=[1, 6], bx=[2, 3, 23], rel=["suimian", "ershier", "sanjie", "jiandao"])
add(id="xinsuo", pin="gen", t="心所（六類）", skt="caitta", en="mental factors (six groups)",
    tier="term", wzq=[("1.3", 3, 3), ("1.3", 9, 14)],
    note_zh="根品進一步分別諸心品中心所俱起之數，如欲界善心品二十二心所，有時增惡作。",
    note_en="The chapter goes on to count which mental factors co-arise in each kind of mind: e.g. a wholesome mind of the sensuous realm has twenty-two, sometimes with remorse added.",
    verse=["受想思觸欲", "於善心品中"], jt=[6], rel=["qishiwu", "xiangying", "ershier"])
add(id="xiangying", pin="gen", t="相應", skt="saṃprayukta", en="association",
    tier="term", wzq=[("1.2", 11, 11)],
    note_zh="心與心所皆屬「有相應」；但心「與心不相應」，因自體不與自體相應。", note_en="Mind and mental factors are both 'associated' dharmas; but mind is not associated with mind, since nothing is associated with itself.",
    verse=["相應義有五"], bx=[75, 76], rel=["xinsuo", "liuyin", "suizeng"])
add(id="buxiangying", pin="gen", t="心不相應行", skt="cittaviprayukta saṃskāra", en="conditionings dissociated from mind",
    tier="term", wzq=[("1.3", 4, 4)],
    verse=["心不相應行"], rel=["de", "sixiang", "erwuxin", "qishiwu"])
add(id="de", pin="gen", t="得・非得", skt="prāpti · aprāpti", en="acquisition · non-acquisition",
    tier="term",
    zh_def="頌曰：「得謂獲成就，非得此相違。」得有二：獲（未得、已失今得）與成就（得已不失）。三世法各有三世得。非得說名異生性。斷惑所證擇滅，其得名離繫得。",
    en_def="'Acquisition is obtaining and possession; non-acquisition is the opposite.' It is either obtaining (what was not had, or was lost, is now had) or possession (what was had is not lost). Dharmas of each time have acquisitions of the three times. Non-acquisition [of the noble path] is called the nature of an ordinary being. The acquisition of a cessation through deliberation reached by abandoning a defilement is the acquisition of disconnection (離繫得).",
    note_zh="《九題》第四、八、九題都建立在「得」之上；第九題專論離繫得。", note_en="Questions 4, 8 and 9 of the Nine Questions all turn on acquisition; Q9 ends with the acquisition of disconnection.",
    verse=["得謂獲成就", "許聖道非得"], jt=[4, 8, 9], bx=[5, 58, 59, 69], rel=["buxiangying", "sixiu", "liran", "shierxin"])
add(id="sixiang", pin="gen", t="有為四相", skt="saṃskṛtalakṣaṇa", en="the characteristics of the conditioned",
    tier="term", wzq=[("1.1", 1, 2)],
    verse=["相謂諸有為"], bx=[97], rel=["sanwuwei", "buxiangying"])
add(id="erwuxin", pin="gen", t="二無心定", skt="asaṃjñi- · nirodha-samāpatti", en="the two mindless attainments",
    tier="term", wzq=[("1.3", 7, 8)],
    zh_extra="無想定：異生依第四靜慮修，誤以無想為解脫；滅盡定：聖者依有頂修，為靜住，由加行得。",
    en_extra="The attainment of non-ideation is cultivated by ordinary beings on the fourth dhyāna, mistaking non-ideation for liberation; the attainment of cessation is cultivated by noble ones on the summit of existence, for peaceful abiding, and is obtained through effort.",
    verse=["如是無想定", "滅盡定亦然"], rel=["buxiangying", "sixiangsiguo", "bajietuo"])
add(id="liuyin", pin="gen", t="六因", skt="ṣaḍ hetavaḥ", en="the six causes",
    tier="hard", wzq=[("3.1", 0, 8)],
    verse=["能作及俱有", "同類因相似"], jt=[1, 3, 9], rel=["siyuan", "wuguo", "bianxing"])
add(id="siyuan", pin="gen", t="四緣", skt="catvāraḥ pratyayāḥ", en="the four conditions",
    tier="hard", wzq=[("3.2", 0, 4)],
    verse=["說有四種緣", "等無間非後"], jt=[3], rel=["liuyin", "wuguo", "shierxin"])
add(id="wuguo", pin="gen", t="五果", skt="pañca phalāni", en="the five fruits",
    tier="hard", wzq=[("3.3", 0, 7)],
    verse=["後因果異熟"], jt=[1], rel=["liuyin", "siyuan", "yishu"])
add(id="shierxin", pin="gen", t="十二心・二十心", skt="dvādaśa cittāni", en="the twelve and twenty minds",
    tier="hard", wzq=[("2.4", 4, 12)],
    mile=("登堂", "Entering the hall"),
    verse=["欲界有四心", "欲界善生九", "三界染心中"], jt=[3, 4], bx=[9], rel=["siyuan", "sanxing", "de"])

# ───────────── 世間品 ─────────────
add(id="sanjie", pin="shi", t="三界・九地", skt="tridhātu · nava bhūmayaḥ", en="three realms and nine stages",
    tier="term", wzq=[("2.1", 0, 1), ("2.1", 6, 7), ("2.1", 12, 12)],
    note_zh="三界九地是全論共用的坐標：幾乎所有問題都要先問「何界何地」。", note_en="The realm-and-stage grid is the coordinate system used throughout the treatise: almost every question starts with 'which realm, which stage?'",
    verse=["地獄傍生鬼"], rel=["sanjiechu", "jinglv", "xunsi", "jinfen"])
add(id="sanjiechu", pin="shi", t="欲界等（三界諸處）", skt="sthāna", en="the places of the three realms",
    tier="term", wzq=[("6.4", 0, 9)],
    verse=["此上十七處"], rel=["sanjie", "wuqu"])
add(id="jinglv", pin="shi", t="四靜慮・四無色（生）", skt="dhyāna · ārūpya (upapatti)", en="the dhyānas and immaterial spheres as places of birth",
    tier="term",
    zh_def="作為生處的四靜慮、四無色（「生靜慮」）。色界十七處分屬四靜慮；無色界無處，由異熟生差別立四處。",
    en_def="The four dhyānas and four immaterial spheres as places of rebirth ('dhyāna by birth'). The seventeen places of the fine-material realm belong to the four dhyānas; the immaterial realm has no places, its four [spheres] being set up by differences in retribution.",
    note_zh="作者：「定靜慮比生靜慮對理解阿毘達磨更重要。」參見定品「生靜慮・定靜慮」。", note_en="The author: dhyāna as meditative attainment matters more than dhyāna as birthplace. See 'dhyāna by birth and by attainment' in the meditation chapter.",
    verse=["無色界無處"], bx=[92], rel=["sanjie", "shengjinglv"])
add(id="qishizhu", pin="shi", t="七識住・九有情居", skt="vijñānasthiti · sattvāvāsa", en="stations of consciousness · abodes of beings",
    tier="term", wzq=[("6.4", 13, 14)], verse=["身異及想異", "是九有情居"], rel=["sanjiechu"])
add(id="siyou", pin="shi", t="四有・中有", skt="bhava · antarābhava", en="the four existences · intermediate existence",
    tier="term", wzq=[("1.1", 23, 25)],
    note_zh="作者：本品「埋藏一些對理解其他部分稍有幫助的細節，尤其是『中有』」。", note_en="The author: this chapter 'hides some details that help with other parts, above all the intermediate existence'.",
    verse=["死生二有中", "於四種有中"], jt=[9], bx=[90], rel=["yuanqi", "sisheng"])
add(id="yuanqi", pin="shi", t="十二支（緣起）", skt="pratītyasamutpāda", en="the twelve links of dependent origination",
    tier="term", wzq=[("6.5", 0, 7)], verse=["如是諸緣起", "宿惑位無明"], rel=["siyou", "jinxing", "sishi"])
add(id="jinxing", pin="shi", t="名等（六觸・十八意近行）", skt="nāma · sparśa · manopavicāra", en="name, the six contacts, the eighteen mental approaches",
    tier="term", wzq=[("6.5", 7, 9)], verse=["名無色四蘊", "從此生六受"], bx=[10, 11, 12], rel=["yuanqi"])
add(id="sishi", pin="shi", t="四食", skt="catvāra āhārāḥ", en="the four foods",
    tier="term", wzq=[("6.6", 0, 1)], verse=["有情由食住"], rel=["yuanqi"])
add(id="wuqu", pin="shi", t="五趣", skt="pañca gatayaḥ", en="the five destinies",
    tier="term", wzq=[("6.4", 10, 10)],
    zh_extra="頌曰：「於中地獄等，自名說五趣，唯無覆無記，有情非中有。」", en_extra="The destinies are only unobscured-indeterminate, belong to beings (not the receptacle world), and exclude the intermediate existence.",
    verse=["自名說五趣"], rel=["sanjiechu", "sisheng"])
add(id="sisheng", pin="shi", t="四生", skt="catasro yonayaḥ", en="the four modes of birth",
    tier="term", wzq=[("6.4", 11, 12)],
    note_zh="根品亦據四生論受生時初得幾根（「欲胎卵濕生，初得二異熟」）。", note_en="The faculties chapter also uses the four modes of birth to ask which faculties are first obtained at rebirth.",
    verse=["於中有四生", "欲胎卵濕生"], rel=["wuqu", "siyou", "ershier"])
add(id="jie_kalpa", pin="shi", t="劫等（四劫・三災・大千）", skt="kalpa", en="eons, calamities, chiliocosms",
    tier="term", wzq=[("6.6", 2, 5)], verse=["應知有四劫", "四大洲日月"], rel=["sanjiechu"])

# ───────────── 業品 ─────────────
add(id="sanye", pin="ye", t="三業", skt="trīṇi karmāṇi", en="the three kinds of action",
    tier="term", wzq=[("3.4", 0, 6)],
    zh_extra="頌曰：「世別由業生，思及思所作。」",
    en_extra="'The variety of the world is born of action: volition and what volition produces.'",
    note_zh="「俱」從業生只說皆從業生，不是「同時」。", note_en="'All [the world's variety] arises from action' — 俱 does not mean 'at the same time'.",
    verse=["世別由業生"], jt=[2], bx=[13, 19, 20], rel=["biaowubiao", "yedao", "dengqi"])
add(id="biaowubiao", pin="ye", t="表・無表", skt="vijñapti · avijñapti", en="informative · non-informative",
    tier="key", wzq=[("3.4", 4, 6), ("3.5", 0, 0), ("3.5", 7, 7)],
    verse=["亂心無心等", "身表許別形"], jt=[2], bx=[14], rel=["sanye", "luyi", "wuyun"])
add(id="dengqi", pin="ye", t="等起・轉隨轉", skt="samutthāna", en="originating mind: 'turning' and 'turning-after'",
    tier="term",
    zh_def="頌曰：「等起有二種，因及彼剎那，如次第應知，名轉名隨轉。」因等起名「轉」，剎那等起名「隨轉」。見所斷識唯轉；五識唯隨轉；修所斷意識通二；無漏、異熟生心俱非。",
    en_def="Originating mind is of two kinds: the causal originator, called 'turning' (轉), and the momentary originator, called 'turning-after' (隨轉). Consciousness abandoned by seeing is only 'turning'; the five sense consciousnesses only 'turning-after'; mind-consciousness abandoned by cultivation may be both; outflow-free and retribution-born minds are neither.",
    verse=["等起有二種", "見斷識唯轉"], rel=["sanye", "biaowubiao"])
add(id="luyi", pin="ye", t="三律儀", skt="saṃvara", en="the three restraints",
    tier="key", wzq=[("3.5", 1, 2), ("3.5", 5, 7)],
    verse=["律儀別解脫", "八成別解脫"], bx=[14, 18], rel=["biejietuo", "deshe", "biaowubiao"])
add(id="biejietuo", pin="ye", t="別解脫等（八種別解脫律儀）", skt="prātimokṣasaṃvara", en="the prātimokṣa restraints",
    tier="term", wzq=[("3.5", 3, 4)],
    zh_extra="別解脫律儀相有八種：苾芻、苾芻尼、正學、勤策、勤策女、近事男、近事女、近住；實體唯四。",
    en_extra="Eight kinds by name (monk, nun, probationer, novice, female novice, layman, laywoman, one-day observer), but only four in substance.",
    verse=["初律儀八種", "立近事近住"], bx=[15, 16], rel=["luyi", "sangui", "deshe"])
add(id="sangui", pin="ye", t="三歸", skt="triśaraṇa", en="the three refuges",
    tier="term",
    zh_def="頌曰：「歸依成佛僧，無學二種法，及涅槃擇滅，是說具三歸。」歸佛，歸依能成佛的無學法；歸僧，歸依成僧的有學、無學法；歸法，歸依涅槃擇滅。",
    en_def="Refuge in the Buddha is refuge in the dharmas beyond training that make a Buddha; in the Saṅgha, in the dharmas of trainees and those beyond training that make the Saṅgha; in the Dharma, in nirvāṇa, cessation through deliberation.",
    verse=["歸依成佛僧"], rel=["biejietuo", "sizhengjing"])
add(id="deshe", pin="ye", t="得捨律儀等", skt="saṃvara-lābha · tyāga", en="obtaining and relinquishing restraint",
    tier="key", wzq=[("3.6", 0, 11)],
    verse=["捨定生善法", "捨別解調伏"], jt=[9], bx=[17], rel=["luyi", "biejietuo", "shengjinglv", "zhongxing"])
add(id="siye", pin="ye", t="曲穢濁等業・四業", skt="kuṭila · doṣa · kaṣāya; catvāri karmāṇi", en="crooked, faulty, turbid actions; the four kinds of action",
    tier="term", wzq=[("3.7", 9, 9)],
    zh_extra="頌曰：「說曲穢濁業，依諂瞋貪生。」",
    en_extra="'Actions called crooked, faulty and turbid arise from deceit, hatred and greed.'",
    verse=["說曲穢濁業", "惡色欲界善"], bx=[21, 22], rel=["sanye", "yedao"])
add(id="yedao", pin="ye", t="十業道", skt="daśa karmapathāḥ", en="the ten courses of action",
    tier="term", wzq=[("3.7", 0, 8)], verse=["所說十業道"], jt=[2], rel=["sanye", "renzhijian"])
add(id="sanzhang", pin="ye", t="三障・五無間業", skt="āvaraṇa · ānantarya", en="the three obstructions · the five deeds of immediate retribution",
    tier="term", wzq=[("6.7", 0, 2)], verse=["三障無間業"], rel=["sanye"])
add(id="liudu", pin="ye", t="六波羅蜜多", skt="ṣaṭ pāramitāḥ", en="the six perfections",
    tier="term", wzq=[("6.7", 3, 3)], verse=["六波羅蜜多"], rel=["fuye"])
add(id="fuye", pin="ye", t="福業事・順福等", skt="puṇyakriyāvastu", en="bases of merit; what is conducive to merit, etc.",
    tier="term", wzq=[("6.7", 4, 5)], verse=["施戒修三類"], rel=["liudu", "shunjuezefen"])
add(id="miao", pin="ye", t="妙等", skt="praṇīta etc.", en="'excellent' and related designations",
    tier="term", wzq=[("6.7", 6, 6)], rel=["sanxing"])

# ───────────── 隨眠品 ─────────────
add(id="suimian", pin="sui", t="六隨眠・九十八隨眠", skt="anuśaya", en="the six and ninety-eight anuśayas",
    tier="term", memo=True, wzq=[("2.2", 0, 12)],
    verse=["隨眠諸有本", "六行部界異"], jt=[6, 7], bx=[23, 26, 27, 28, 36], rel=["jiansuoduan", "bianxing", "suizeng", "lou"])
add(id="bianxing", pin="sui", t="遍行惑", skt="sarvatraga", en="the universal defilements",
    tier="term",
    zh_def="頌曰：「見苦集所斷，諸見疑相應，及不共無明，遍行自界地。」即見苦所斷七（五見、疑、無明）與見集所斷四（邪見、見取、疑、無明），三界各十一。其中除身見、邊見，餘九能遍緣上地。",
    en_def="The defilements abandoned by seeing suffering and origin that are views, doubt, the ignorance associated with them, and unique ignorance, are universal within their own realm and stage: seven abandoned by seeing suffering and four by seeing origin, eleven in each realm. Excluding self-view and extreme view, nine of them can also take higher stages as object.",
    verse=["見苦集所斷", "於中除二見"], jt=[1, 7], bx=[31, 32, 85], rel=["suimian", "liuyin", "suizeng"])
add(id="suizeng", pin="sui", t="隨增", skt="anuśayana", en="adhering-and-growing",
    tier="key", wzq=[("1.1", 6, 7)],
    mile=("入室", "Entering the inner room"),
    verse=["於彼漏隨增"], jt=[6, 7], bx=[33, 34], rel=["suimian", "youlou", "yousuimianxin", "xiangying"])
add(id="sanshi", pin="sui", t="一切有（三世實有）", skt="sarvāstitva", en="'all exists': the reality of the three times",
    tier="term",
    zh_def="頌曰：「三世有由說，二有境果故，說三世有故，許說一切有。」以契經說、二緣生識、識必有境、已謝業能有果為證，許過去未來實有，故名說一切有部。",
    en_def="'The three times exist, because [the Buddha] said so, because [consciousness arises from] two, because [consciousness] has an object, and because [past action] has a fruit. Because it teaches that the three times exist, it is accepted as the [school that] teaches that all exists.'",
    verse=["三世有由說"], rel=["suimian", "sixiang"])
add(id="yousuimianxin", pin="sui", t="有隨眠心", skt="sānuśaya citta", en="mind with anuśaya",
    tier="term",
    zh_def="頌曰：「有隨眠心二，謂有染無染，有染心通二，無染局隨增。」有染心既與隨眠相應，又為其所緣；無染心不與隨眠相應，隨眠於彼唯所緣隨增。",
    en_def="Minds with anuśaya are of two kinds, defiled and undefiled. A defiled mind is so in both ways (associated with anuśayas and their object); an undefiled mind is not associated with anuśayas, which adhere-and-grow in it only as object.",
    verse=["有隨眠心二"], bx=[33], rel=["suizeng", "youlou"])
add(id="lou", pin="sui", t="漏等（漏・瀑流・軛・取・結縛）", skt="āsrava · ogha · yoga · upādāna · saṃyojana", en="outflows, floods, yokes, graspings, fetters",
    tier="term",
    zh_def="隨眠又立為三漏、四瀑流、四軛、四取，以及九結、三縛、五順下分結、五順上分結、隨煩惱、十纏等異門。頌曰：「欲有軛并癡，見分二名取。」",
    en_def="The anuśayas are regrouped as the three outflows, four floods, four yokes, four graspings, and as fetters, bonds, the five lower and five higher fetters, secondary defilements and the ten envelopers.",
    verse=["欲有軛并癡", "順上分亦五"], jt=[7], bx=[35], rel=["suimian", "youlou"])
add(id="siduizhi", pin="sui", t="四對治", skt="caturvidha pratipakṣa", en="the four kinds of counteraction",
    tier="term",
    zh_def="頌曰：「對治有四種，謂斷持遠厭。」斷對治（無間道）、持對治（解脫道）、遠分對治（解脫道後所起道）、厭患對治（見此界過失、深生厭患之道）。",
    en_def="Counteraction by abandoning (the uninterrupted path), by maintaining (the path of liberation), by distancing (the path arising after the path of liberation), and by disgust (a path that sees the faults of this realm and is deeply disgusted with it).",
    verse=["對治有四種"], rel=["sidao", "liran"])
add(id="jiubianzhi", pin="sui", t="九遍知", skt="nava parijñāḥ", en="the nine thorough knowledges",
    tier="key",
    zh_def="斷惑之果立為九遍知：欲界見苦集所斷盡、色無色界見苦集所斷盡、欲界見滅所斷盡、色無色界見滅所斷盡、欲界見道所斷盡、色無色界見道所斷盡、五順下分結盡、色愛盡、一切結盡。",
    en_def="The results of abandoning defilements are set up as nine thorough knowledges: the destruction of what is abandoned by seeing suffering and origin in the sensuous realm; the same in the higher realms; by seeing cessation, sensuous realm; the same, higher realms; by seeing the path, sensuous realm; the same, higher realms; the destruction of the five lower fetters; of greed for the fine-material; of all fetters.",
    note_zh="作者：「四果和九遍知的安立，和定品、隨眠品關係密切。」英譯本在遍知「捨得」處錯誤較多。", note_en="The author: how the four fruits and nine thorough knowledges are established is closely tied to the meditation and anuśaya chapters. The English translations err repeatedly on which knowledges are relinquished and obtained.",
    verse=["斷遍知有九", "得無漏斷得"], bx=[37, 38, 39, 40, 41, 42, 43, 44, 45], rel=["sixiangsiguo", "liran", "suimian"])

# ───────────── 賢聖品 ─────────────
add(id="sishengzhong", pin="xian", t="四聖種", skt="catvāra āryavaṃśāḥ", en="the four lineages of the noble ones",
    tier="term",
    zh_def="於衣服、飲食、臥具隨所得喜足，及樂斷樂修。頌曰：「四聖種亦爾，前三唯喜足。」其性皆無貪。",
    en_def="Contentment with whatever robes, food and lodging one gets, and delight in abandoning and cultivating. Their nature is non-greed; the first three are contentment.",
    verse=["四聖種亦爾"], rel=["yaoermen", "sanhui"])
add(id="yaoermen", pin="xian", t="要二門（不淨觀・息念）", skt="aśubhā · ānāpānasmṛti", en="the two gates: contemplation of the foul, mindfulness of breathing",
    tier="term", wzq=[("5.1", 2, 3)],
    note_zh="作者舉為「包含的內容很少」的術語之一。", note_en="The author cites this as one of the terms that contain little.",
    verse=["入修要二門"], rel=["sinianzhu", "sanhui"])
add(id="sanhui", pin="xian", t="聞所成慧等（三慧）", skt="śruta- · cintā- · bhāvanā-mayī prajñā", en="understanding born of hearing, reflection, cultivation",
    tier="term", wzq=[("5.1", 0, 1)], verse=["聞思修所成"], bx=[78, 79, 80], rel=["sinianzhu", "shunjuezefen"])
add(id="sinianzhu", pin="xian", t="四念住", skt="catvāri smṛtyupasthānāni", en="the four applications of mindfulness",
    tier="term", wzq=[("5.1", 4, 6)], verse=["依已修成止"], rel=["sanhui", "shunjuezefen", "sanshiqi"])
add(id="shiliu", pin="xian", t="十六行相", skt="ṣoḍaśākārāḥ", en="the sixteen aspects",
    tier="term", wzq=[("1.1", 18, 22)], verse=["從此生煖法"], rel=["sidi", "shunjuezefen", "sansanmodi"])
add(id="shunjuezefen", pin="xian", t="順決擇分（四善根）", skt="nirvedhabhāgīya", en="the aids to penetration (four wholesome roots)",
    tier="term", wzq=[("5.2", 0, 9)], verse=["從此生煖法", "前順解脫分"], jt=[9], bx=[46, 47, 48, 49], rel=["shiliu", "jiandao", "zhongxing"])
add(id="jiandao", pin="xian", t="見道等（聖諦現觀）", skt="darśanamārga · abhisamaya", en="the path of seeing (direct realization)",
    tier="term", wzq=[("5.3", 0, 7)],
    note_zh="常見誤解：把見道說成十六剎那，或以為見道即須陀洹向。實則見道唯前十五心，第十六心道類智已屬修道；住見道者亦可是一來向、不還向。",
    note_en="Common errors: taking the path of seeing as sixteen moments, or equating it with the candidate for stream-entry. It is only the first fifteen moments (the sixteenth, subsequent knowledge of the path, belongs to the path of cultivation), and one on it may be a candidate for once-returning or non-returning.",
    verse=["前十五見道", "見道唯無漏"], jt=[8, 9], bx=[24, 50, 67, 68, 69], rel=["sixiangsiguo", "shunjuezefen", "renzhijian"])
add(id="sixiangsiguo", pin="xian", t="四向四果", skt="catvāraḥ pratipannakāḥ · phalasthāḥ", en="four candidates and four fruits",
    tier="key", wzq=[("5.4", 0, 9)],
    verse=["諸得果位中", "斷欲三四品", "斷七或八品"], jt=[8], bx=[51, 52, 53, 54, 56], rel=["jiandao", "jiubianzhi", "liran", "zhongxing"])
add(id="shamenxing", pin="xian", t="沙門性", skt="śrāmaṇya", en="the state of a renunciant",
    tier="term",
    zh_def="頌曰：「淨道沙門性，有為無為果，此有八十九，解脫道及滅。」無漏道名沙門性；其果有有為（解脫道）、無為（擇滅）二種，各有八十九。",
    en_def="The pure (outflow-free) path is the state of a renunciant; its fruits are conditioned (paths of liberation) and unconditioned (cessations), eighty-nine of each.",
    verse=["淨道沙門性"], rel=["sixiangsiguo", "sidao"])
add(id="zhongxing", pin="xian", t="種性等（六種性・練根）", skt="gotra · indriyasañcāra", en="lineages and the refinement of faculties",
    tier="term", wzq=[("5.5", 0, 5)],
    note_zh="「根」只有鈍、利二種，「種性」有六種：前五皆鈍根，每轉一種性各需一無間道一解脫道。", note_en="There are only two kinds of faculty (dull, sharp) but six lineages, the first five all dull; each change of lineage needs its own uninterrupted and liberation path.",
    verse=["阿羅漢有六"], jt=[9], bx=[55, 60, 61, 62, 63, 64], rel=["sixiangsiguo", "deshe", "sidao"])
add(id="sidao", pin="xian", t="四道", skt="catvāro mārgāḥ", en="the four paths",
    tier="term", wzq=[("5.5", 8, 10)], verse=["應知一切道"], bx=[65], rel=["siduizhi", "liran", "zhongxing"])
add(id="sanshiqi", pin="xian", t="三十七覺分", skt="saptatriṃśad bodhipakṣyāḥ", en="the thirty-seven factors of awakening",
    tier="term", memo=True, wzq=[("6.1", 0, 8), ("6.1", 19, 20)], verse=["覺分三十七", "初靜慮一切"], bx=[66], rel=["sinianzhu", "ershier", "sizhengjing"])
add(id="sizhengjing", pin="xian", t="四證淨", skt="avetyaprasāda", en="faith born of realization",
    tier="term", wzq=[("6.2", 0, 4)], verse=["證淨有四種"], rel=["sanshiqi", "sangui"])
add(id="xuezhi", pin="xian", t="學支等（無學十支）", skt="śaikṣāṅga · aśaikṣāṅga", en="factors of trainees and of those beyond training",
    tier="term", wzq=[("6.3", 0, 4)], verse=["有為無學支"], rel=["sanshiqi", "sixiangsiguo"])

# ───────────── 智品 ─────────────
add(id="renzhijian", pin="zhi", t="忍智見慧", skt="kṣānti · jñāna · dṛṣṭi · prajñā", en="receptivity, knowledge, view, understanding",
    tier="term", wzq=[("2.6", 0, 6)], verse=["聖慧忍非智"], jt=[2], bx=[50], rel=["shizhi", "jiandao", "yedao"])
add(id="shizhi", pin="zhi", t="十智", skt="daśa jñānāni", en="the ten knowledges",
    tier="key", wzq=[("2.5", 0, 7)], verse=["智十總有二", "世俗遍為境"], bx=[70, 71, 72, 73, 74, 77], rel=["renzhijian", "liutong", "sixiu"])
add(id="xianguanbian", pin="zhi", t="現觀邊俗智", skt="abhisamayāntika saṃvṛtijñāna", en="conventional knowledge 'at the edge of' direct realization",
    tier="term",
    zh_def="頌曰：「見道忍智起，即彼未來修，三類智兼修，現觀邊俗智。」見道中各忍智生起時，修同類未來忍智；至苦、集、滅類智時，兼修未來世俗智，名現觀邊俗智。",
    en_def="On the path of seeing, as each receptivity and knowledge arises, the future ones of the same kind are cultivated; at the subsequent knowledges of suffering, origin and cessation, future conventional knowledge is also cultivated: this is called conventional knowledge at the edge of direct realization.",
    verse=["見道忍智起"], rel=["shizhi", "sixiu", "jiandao"])
add(id="sixiu", pin="zhi", t="四修（得修・習修）", skt="bhāvanā", en="the kinds of cultivation (by acquisition, by practice…)",
    tier="hard",
    zh_def="頌曰：「立得修習修，依善有為法，依諸有漏法，立治修遣修。」得修、習修依善有為法立；治修、遣修依有漏法立。另有防修、觀修，迦濕彌羅師說攝入治、遣二修。",
    en_def="Cultivation by acquisition and by practice are established for wholesome conditioned dharmas; cultivation by counteraction and by expulsion for with-outflow dharmas. Cultivation by guarding and by inspection are, for the Kashmiri masters, included in the latter two.",
    mile=("由陸入海", "From land into the ocean"),
    verse=["立得修習修"], jt=[8], bx=[81, 82], rel=["de", "shizhi", "weijingwulou", "liran"])
add(id="bugong", pin="zhi", t="十八不共法", skt="āveṇikā buddhadharmāḥ", en="the eighteen exclusive qualities",
    tier="term", wzq=[("4.5", 0, 5)], verse=["十八不共法"], bx=[83], rel=["wuzheng", "liutong"])
add(id="wuzheng", pin="zhi", t="無諍等（願智・四無礙解・邊際定）", skt="araṇā · praṇidhijñāna · pratisaṃvid", en="non-contention, knowledge by resolve, analytical knowledges",
    tier="term", wzq=[("4.5", 6, 13)], verse=["無諍世俗智", "六依邊際得"], rel=["bugong", "shizhi"])
add(id="liutong", pin="zhi", t="六通・三明・三示導", skt="ṣaḍ abhijñāḥ", en="the six supernormal powers",
    tier="key", wzq=[("4.4", 0, 10)], verse=["通六謂神境", "第五二六明"], bx=[86, 87, 88, 89, 90], rel=["shizhi", "bugong", "chanzhi"])

# ───────────── 定品 ─────────────
add(id="chanzhi", pin="ding", t="靜慮支", skt="dhyānāṅga", en="the factors of the dhyānas",
    tier="term",
    zh_def="初靜慮五支：尋、伺、喜、樂、三摩地；第二靜慮四支：內等淨、喜、樂、三摩地；第三靜慮五支：行捨、念、慧、樂、三摩地；第四靜慮四支：不苦不樂受、捨清淨、念清淨、三摩地。共十八支，實事十一。頌曰：「初具伺喜樂，後漸離前支。」",
    en_def="First dhyāna, five factors (vitarka, vicāra, joy, pleasure, concentration); second, four (inner clarity, joy, pleasure, concentration); third, five (equanimity, mindfulness, understanding, pleasure, concentration); fourth, four (neither-pain-nor-pleasure, purity of equanimity, purity of mindfulness, concentration). Eighteen by name, eleven real entities.",
    note_zh="作者：「禪支等是比較有意思的。」", note_en="The author: the dhyāna factors 'are rather interesting'.",
    verse=["初具伺喜樂"], rel=["shengjinglv", "weijingwulou", "xunsi"])
add(id="weijingwulou", pin="ding", t="味・淨・無漏（等至）", skt="āsvādana · śuddhaka · anāsrava", en="savouring, pure and outflow-free attainments",
    tier="term", wzq=[("4.1", 0, 7)],
    note_zh="此「淨」是有漏善（śuddhaka），不是無漏。英譯以 pure 對譯時須留意。", note_en="'Pure' (śuddhaka) here means with-outflow wholesome, not outflow-free; beware where translations use 'pure' for anāsrava elsewhere.",
    verse=["此本等至八"], jt=[8], bx=[93, 94, 95, 96], rel=["chanzhi", "shuntuifen", "sixiu"])
add(id="shuntuifen", pin="ding", t="順退分等（四種淨定）", skt="hānabhāgīya etc.", en="pure concentration conducive to decline, stability, progress, penetration",
    tier="term", wzq=[("5.2", 1, 2)], verse=["淨定有四種"], rel=["weijingwulou", "shunjuezefen"])
add(id="jinfen", pin="ding", t="近分（未至定）", skt="sāmantaka · anāgamya", en="preparatory stages (the not-yet-arrived)",
    tier="term",
    zh_def="八根本等至各有近分，初靜慮近分名未至定。近分唯捨受相應；未至定通淨、無漏，餘七近分唯淨。世俗道離下地染，皆依近分起。",
    en_def="Each of the eight fundamental attainments has a preparatory stage; that of the first dhyāna is the not-yet-arrived concentration. Preparatory stages are associated only with equanimity; the not-yet-arrived may be pure or outflow-free, the other seven only pure. Worldly detachment from a lower stage is always done in the preparatory stage.",
    verse=["近分八捨淨", "近分離下染"], rel=["liran", "sanjie", "zhongjinglv"])
add(id="zhongjinglv", pin="ding", t="中靜慮（靜慮中間）", skt="dhyānāntara", en="the intermediate dhyāna",
    tier="term",
    zh_def="頌曰：「中靜慮無尋，具三唯捨受。」初、二靜慮之間，無尋唯伺，通味、淨、無漏三種，唯捨受相應。",
    en_def="Between the first and second dhyānas: without vitarka but with vicāra, of all three kinds (savouring, pure, outflow-free), associated only with equanimity.",
    verse=["中靜慮無尋"], bx=[91], rel=["xunsi", "jinfen"])
add(id="sansanmodi", pin="ding", t="空無相無願等（三三摩地）", skt="śūnyatā · ānimitta · apraṇihita", en="emptiness, signlessness, wishlessness",
    tier="term", wzq=[("4.2", 0, 9)], verse=["空謂空非我", "此通淨無漏"], bx=[98], rel=["shiliu", "weijingwulou"])
add(id="sixiuding", pin="ding", t="四修定", skt="samādhibhāvanā", en="the four cultivations of concentration",
    tier="term",
    zh_def="頌曰：「為得現法樂，修諸善靜慮，為得勝知見，修淨天眼通，為得分別慧，修諸加行善，為得諸漏盡，修金剛喻定。」",
    en_def="Cultivating wholesome dhyāna for a pleasant abiding in this life; the divine eye for superior knowledge and vision; wholesome dharmas from effort for discriminating understanding; the diamond-like concentration for the destruction of the outflows.",
    verse=["為得現法樂"], rel=["liutong", "weijingwulou"])
add(id="siwuliang", pin="ding", t="四無量", skt="catvāry apramāṇāni", en="the four immeasurables",
    tier="term", wzq=[("4.3", 0, 1)], verse=["無量有四種"], bx=[99], rel=["bajietuo"])
add(id="bajietuo", pin="ding", t="八解脫等（八勝處・十遍處）", skt="vimokṣa · abhibhvāyatana · kṛtsnāyatana", en="liberations, spheres of mastery, totality spheres",
    tier="term", wzq=[("4.3", 2, 7)], verse=["勝處有八種", "遍處有十種"], bx=[84], rel=["siwuliang", "erwuxin"])
add(id="shengjinglv", pin="ding", t="生靜慮・定靜慮", skt="upapatti- · samāpatti-dhyāna", en="dhyāna by birth and by attainment",
    tier="key",
    zh_def="頌曰：「靜慮四各二。」四靜慮各有生、定二種：生靜慮指生於靜慮地者的諸蘊，定靜慮指入定所起的等至。定品所論主要是定靜慮。",
    en_def="'Each of the four dhyānas is twofold.' Each is either by birth (the aggregates of beings born in that stage) or by attainment (the meditative attainment itself). The meditation chapter mainly treats the latter.",
    verse=["靜慮四各二"], bx=[92], rel=["jinglv", "chanzhi", "liran"])
add(id="liran", pin="ding", t="離染", skt="vairāgya", en="detachment",
    tier="key",
    zh_def="斷某地修所斷惑，須斷九品（上上至下下），各以無間道斷、解脫道證。異生唯以世俗道離染（依近分，厭下欣上）；聖者可以世俗道或無漏道離染，唯有頂須以無漏道。頌曰：「有頂由無漏，餘由二離染，聖二離八修，各二離繫得。」",
    en_def="To abandon the defilements of a stage that are abandoned by cultivation one cuts nine grades, each by an uninterrupted path and confirmed by a path of liberation. Ordinary beings detach only by the worldly path (in the preparatory stage, disgusted with the lower, delighting in the higher); noble ones may use either the worldly or the outflow-free path, except for the summit of existence, which requires the outflow-free path.",
    verse=["有頂由無漏", "近分離下染"], jt=[4, 5, 8, 9], bx=[25, 57, 59], rel=["sixiangsiguo", "jinfen", "jiubianzhi", "de"])
