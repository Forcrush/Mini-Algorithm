# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-08-17 22:18:58
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-08-18 17:03:52


class Solution:
    def findLadders(self, beginWord, endWord, wordList):

        if not endWord in wordList: return []

        import collections

        def neighboor(word):
            for i in range(len(word)):
                for newWord in pattern_to_word[word[:i]+'*'+word[i+1:]]:
                    if newWord not in marked:
                        yield newWord

        def findPath(end):
            res = []
            for curr in end:
                for parent in path[curr[0]]:
                    res.append([parent]+curr)
            return res

        pattern_to_word = collections.defaultdict(list)
        for w in wordList:
            for i in range(len(w)):
                pattern_to_word[w[:i]+"*"+w[i+1:]].append(w)

        marked = set()
        path = collections.defaultdict(set)
        begin = set([beginWord])
        end = set([endWord])
        forward = True
        while begin and end:
        	# 哪边遍历的节点少就遍历哪边 不一定交替遍历
            if len(begin) > len(end):
                begin, end = end, begin
                forward = not forward

            temp = set()
            for word in begin:
                marked.add(word)
            for word in begin:
                for w in neighboor(word):
                    temp.add(w)
                    if forward:
                        path[w].add(word)
                    else:
                        path[word].add(w)
            begin = temp

            # 出现交集 所有的最短路径已经找到
            if begin & end:
                res = [[endWord]]
                # 根据储存的节点向前回溯
                while res[0][0] != beginWord:
                    res = findPath(res)
                return res
        return []


'''
beginWord = "raining"
endWord = "cellini"
wordList = ["heaping","conning","nipping","wadding","pulling","lunging","figging","donning","jamming","coating","foaling","ousting","dowsing","busting","penning","lapping","yanking","sapping","tasking","rigging","ranking","larking","farming","dunging","nutting","gouging","barfing","fasting","belting","boiling","boating","dipping","kilning","barking","furling","calving","veiling","decking","ricking","salting","lucking","sending","taiping","marking","martina","warping","bulking","seaming","topping","larding","jilting","besting","weeding","nesting","baiting","jibbing","pelting","bushing","garbing","banting","keeping","venting","rapping","binning","mulling","smiting","hatting","tapping","writing","footing","carding","ratting","bagging","sitting","dousing","pinking","testing","passing","gelling","gassing","ranging","hefting","vamping","wetting","paining","rolling","sinking","yakking","shaking","nabbing","licking","sparing","hamming","celling","halving","matting","landing","kooking","pinning","hagging","narking","soaping","winding","dealing","earring","cunning","moating","skiting","jutting","fueling","hooping","guiling","mapping","hailing","gutting","firming","bunting","mealing","rending","jobbing","pauling","foiling","peeking","rollins","lansing","felling","whiting","vealing","resting","saltine","earning","purging","mullins","pausing","colling","banning","wasting","sealing","gigging","scaring","pocking","massing","curring","storing","dinging","handing","pitting","faining","cupping","staring","riffing","gowning","hipping","vanning","darting","maiming","damping","deaning","bellini","kipling","marting","hawking","fending","kicking","beading","curving","wending","yelling","foaming","rifting","surging","gaining","stoking","panging","winking","nursing","oinking","looking","tolling","bailing","tanking","hacking","warming","cooping","wanting","rotting","kinking","bugging","purling","wincing","joining","belling","wilting","tensing","fellini","wilding","binding","bugling","sagging","nagging","binging","tatting","cellini","silting","belying","ripping","crating","slaking","killing","hurting","running","harming","banding","rinking","staying","touting","hasting","melting","nibbing","talking","ganging","bonging","rilling","damning","pooling","porting","sinning","collins","barbing","bunking","smiling","hanging","tending","bulging","ginning","coiling","lolling","molting","letting","mending","hinging","gunning","melding","dilling","shaving","harping","basting","cobbing","carting","leading","styling","fowling","goading","yowling","zipping","wagging","gaoling","panning","valving","peeling","titling","sailing","harding","parring","haloing","quiting","punting","reeling","batting","signing","pegging","bogging","mashing","rankine","seeding","sassing","wafting","winging","framing","rooting","longing","sabling","bulbing","whiling","balking","canting","dashing","dueling","renting","booting","whaling","vatting","veining","fencing","yucking","slaving","welling","sunning","lulling","purring","dawning","sensing","meaning","wording","hogging","parsing","falling","yelping","dinning","vetting","hulling","reading","lapsing","tooling","hoaxing","roiling","forming","ramming","gelding","felting","popping","walling","costing","welding","washing","filling","lasting","couping","cabling","getting","winning","carping","martins","bilking","burning","jelling","sicking","tinting","ceiling","totting","balding","kenning","tinging","hugging","westing","burring","pasting","pecking","parking","slaying","pigging","heating","manning","bucking","bussing","gagging","goaling","rowling","netting","funking","pitying","jarring","tasting","putting","beating","funding","mauling","balling","molding","shining","perkins","dialing","panting","looping","welting","relying","dulling","dumping","tanning","warring","gatling","staging","finding","farting","petting","picking","swaying","toiling","jambing","bawling","minting","wedding","hulking","keeling","nanking","railing","heading","cutting","gosling","vesting","sighing","mucking","copping","polling","raising","fooling","hooting","titting","calming","seating","rifling","soiling","dubbing","jesting","posting","sacking","corking","yipping","lathing","bopping","setting","coaxing","poshing","fawning","heeling","warning","napping","vending","mooting","hurling","supping","nanjing","pipping","tagging","mopping","souping","palming","gulling","kirking","gilding","docking","wefting","dusting","sharing","darling","bowling","lauding","bidding","hopping","honking","hunting","pepping","busying","damming","patting","hitting","gusting","jigging","gabbing","hosting","sidling","telling","rusting","daubing","reining","memling","healing","gashing","betting","lilting","hashing","salving","firring","gabling","ducking","waiving","skating","worming","waiting","burying","booking","corning","suiting","hooking","gonging","listing","hulaing","sulking","digging","fouling","zincing","cocking","packing","scaling","pooping","zinging","banging","bolling","punning","palling","sipping","bunging","minding","choking","yapping","nicking","warding","gorging","canning","culling","lending","spaying","lashing","pupping","fanning","banking","pinging","roaming","sopping","fonding","searing","fucking","rooking","tooting","raining","billing","pulsing","curbing","cashing","calking","harking","tarring","tacking","whining","tarting","pauline","rasping","howling","helling","curling","pucking","hauling","coaling","lopping","mailing","wailing","lugging","ticking","staving","snaking","selling","masking","jabbing","mewling","heaving","soaring","fagging","cording","begging","ridging","jetting","backing","dotting","lacking","parting","jotting","dunning","tinning","stiling","stating","zapping","hearing","fitting","barging","galling","wigging","feeding","tenting","looting","cabbing","cursing","dunking","dabbing","ragging","bedding","witting","pouting","burping","slating","tamping","basking","failing","papping","narcing","lancing","furlong","tabling","dolling","tailing","pawning","collies","lamming","coifing","bolting","sucking","rafting","morning","ranting","tabbing","rinding","bandung","bashing","bending","ducting","casting","camping","flaming","hinting","sanding","carving","lagging","helping","keening","jolting","temping","junking","manging","dimming","ringing","tipping","spiking","malling","pursing","soaking","willing","fulling","causing","jacking","furring","singing","halting","tucking","ruining","denting","calling","barring","fopping","yawning","tilling","nilling","downing","cooling","martini","budging","lapwing","mincing","rinsing","cowling","marring","coining","sibling","potting","tauting","bulling","lurking","sorting","poohing","bathing","spicing","nailing","spiting","racking","lusting","rutting","gulping","tilting","pairing","peaking","capping","gobbing","finking"]
print(Solution().findLadders(beginWord, endWord, wordList))
'''