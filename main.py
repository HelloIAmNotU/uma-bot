import io
import random
import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import time
from PIL import Image, ImageDraw, ImageFont
from urllib.request import urlopen
names = [f"bamboo memory",
         f"biko pegasus",
         f"biwa hayahide",
         f"calstone light o",
         f"cheval grand",
         f"curren chan",
         f"daiichi ruby",
         f"daitaku helios",
         f"daiwa scarlet",
         f"dantsu flame",
         f"dream journey",
         f"duramente",
         f"durandal",
         f"eishin flash",
         f"el condor pasa",
         f"fenomeno",
         f"fine motion",
         f"fuji kiseki",
         f"gentildonna",
         f"gold city",
         f"gold ship",
         f"grass wonder",
         f"haru urara",
         f"hishi akebono",
         f"hishi amazon",
         f"admire vega",
         f"agnes digital",
         f"agnes tachyon",
         f"air groove",
         f"almond eye",
         f"aston machan",
         f"ikuno dictus",
         f"inari one",
         f"ines fujin",
         f"jungle pocket",
         f"katsuragi ace",
         f"kawakami princess",
         f"king halo",
         f"kitasan black",
         f"manhattan cafe",
         f"maruzensky",
         f"marvelous sunday",
         f"matikanefukukitaru",
         f"matikanetannhauser",
         f"mayano top gun",
         f"meisho doto",
         f"mejiro ardan",
         f"mejiro dober",
         f"mejiro mcqueen",
         f"mejiro palmer",
         f"mejiro ryan",
         f"mihono bourbon",
         f"mr cb",
         f"nakayama festa",
         f"narita brian",
         f"narita taishin",
         f"narita top road",
         f"nice nature",
         f"nishino flower",
         f"oguri cap",
         f"orfevre",
         f"rice shower",
         f"sakura bakushin o",
         f"sakura chiyono o",
         f"satono crown",
         f"satono diamond",
         f"seeking the pearl",
         f"seiun sky",
         f"shinko windy",
         f"silence suzuka",
         f"sirius symboli",
         f"smart falcon",
         f"special week",
         f"stay gold",
         f"still in love",
         f"super creek",
         f"sweep tosho",
         f"symboli kris s",
         f"symboli rudolf",
         f"tm opera o",
         f"taiki shuttle",
         f"tamamo cross",
         f"tanino gimlet",
         f"tokai teio",
         f"tosen jordan",
         f"transcend",
         f"twin turbo",
         f"vivlos",
         f"vodka",
         f"winning ticket",
         f"yaeno muteki",
         f"yukino bijin",
         f"zenno rob roy",
         f"no reason"]
images = [
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450305815079813160/thumb.png?ex=69420e0b&is=6940bc8b&hm=dff5e1c8c6e6083d17a2547ff886d481e724a1fd2c8dd4d3ec71b41fc7f3ceda&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450305831043203104/thumb.png?ex=69420e0f&is=6940bc8f&hm=0ae7e61c3d0c2f5f1f56dc3e28d699ad11163626761d14ee9ba2066850ba2933&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450305911104077877/thumb.png?ex=69420e22&is=6940bca2&hm=6edbe994e956c29ac7e6b0f9b64b169ae51b42255ed5999957acab749bcb91f6&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450305934680133724/thumb.png?ex=69420e28&is=6940bca8&hm=3aed5272df0f76c8544a67a1639e4d258f5cd42ab96fe267113cf47769b6eb05&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450305998488338452/thumb.png?ex=69420e37&is=6940bcb7&hm=47bf02873f1402900d6b748e2f64055a804207ca461fd2d0c68f572e7c46e93d&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450306021645091119/thumb.png?ex=69420e3c&is=6940bcbc&hm=41a0e7fea638e06305bb7b6cfa38617889ad09d3898f7413c9595608aad68570&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450306040406081678/thumb.png?ex=69420e41&is=6940bcc1&hm=551e6bb16a2f1b4b0c266269734543a1777b18a7a984778c37427a9926e56e5d&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450306066578542744/thumb.png?ex=69420e47&is=6940bcc7&hm=31116ed42c9f52294833bd785f61e989f334a9c0cb0f0a583b5e1178f52ccd94&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450306089001156701/thumb.png?ex=69420e4d&is=6940bccd&hm=9f1183d8959875e0f34b22bbd0150af77a165c3fc7b53e74187e1debcc500620&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450306267061944381/thumb.png?ex=69420e77&is=6940bcf7&hm=cb38c5be462c4888c0f0be98cc928c749ca08c65517c183c93e734771dd94664&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450306288561950760/thumb.png?ex=69420e7c&is=6940bcfc&hm=cd2b5bdecf1b052a99f25b23afeabc555782ee993801a90f5cb52e7c5e7e2083&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450306321802068090/thumb.png?ex=69420e84&is=6940bd04&hm=8ef77070a3c4befb08b3fb66cc173949425dd83e6d23e67a24352c30b2219d87&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450306372980965407/thumb.png?ex=69420e90&is=6940bd10&hm=0033f339873e6727b90b62ef2a5a96a84aaa35fac5a4e995ea076f71e030ca90&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450306389472710818/thumb.png?ex=69420e94&is=6940bd14&hm=eed87083ab730ae9a4930029df6d3f719c1632844a9ee25991281ea489e8ad0a&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450306421269991605/thumb.png?ex=69420e9c&is=6940bd1c&hm=1e7457d8fae5abb43a57fbe946a189dfed4789b9fb2f50108d97470b18ed52bb&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450306464638963753/thumb.png?ex=69420ea6&is=6940bd26&hm=08ba6b4a463db2ee0c034d74525c08911e1980b7a929eb74e815506371f67efe&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450306497203667016/thumb.png?ex=69420eae&is=6940bd2e&hm=63f1b8cd79d4f5fb6ccafd064dbcb0984bb284d65488cbdbb18b6639c8f27088&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450306519278161973/thumb.png?ex=69420eb3&is=6940bd33&hm=21f5829c268a58e530b709e8512f3378ec5acfaa2d25f8d26b870bd49cb69103&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450306537657602048/thumb.png?ex=69420eb7&is=6940bd37&hm=ef38b929608218c13e9b3d292831954647776d2eb15134b98a7ebaaa2034885e&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450306552618549268/thumb.png?ex=69420ebb&is=6940bd3b&hm=cdd009848d059138e40ddca53ee517eb5fef2ecce23d9fd3fa0d6a922eda76eb&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450306567357595680/thumb.png?ex=69420ebf&is=6940bd3f&hm=593d280b98df4dedbf192cba04df40680c623f53db6c6f44441f799cca6f053b&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450306582754889882/thumb.png?ex=69420ec2&is=6940bd42&hm=5e5228901f4a490625be685591f57fba4f99f9ec8d4df71bfbca60983ba88b13&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450306592896450671/thumb.png?ex=69420ec5&is=6940bd45&hm=179eec4ee5bedd6ebd3d37c4bbbcadf0ced4823555f27f225057f7e6eb8a1fb3&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450306601490579537/thumb.png?ex=69420ec7&is=6940bd47&hm=b4b5131f2b518d2f648ab48820ed73ac7feab608b8d55646695ede951e0c8dd2&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450306615403089990/thumb.png?ex=69420eca&is=6940bd4a&hm=1103b4ea66496aa162f950d9483412889f1221bc7282881bf7ba5f4f304ca559&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450306778695729152/thumb.png?ex=69420ef1&is=6940bd71&hm=803a632b39de8e3bb372436169f9cb4bca641e26a4d92fce848b159c0f273e3c&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450306785595490307/thumb.png?ex=69420ef3&is=6940bd73&hm=d38f34987a3d8df407a7012e475d15a8e0da4c50b6ab22cd4ed869ea0c776959&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450306795254845481/thumb.png?ex=69420ef5&is=6940bd75&hm=ef61a65ba4e51d93f5838fd5ec64c0c920d8c50832bcbbc0aeb5fe81773c0140&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450306805291810868/thumb.png?ex=69420ef7&is=6940bd77&hm=dcdc02264425323d2eaf7dbacf8dda9b03c69e9533df406699b94afde86d587e&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450306818680295424/thumb.png?ex=69420efa&is=6940bd7a&hm=7f333fe0716ca171c1a127cd8c1e93b4ece6997ba6803b116005e8d85edac464&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450306830981926983/thumb.png?ex=69420efd&is=6940bd7d&hm=082e5c1de8feb316566759fd07ec75bc6599b06c28b8d59dc60ac5920bccd440&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450307136813928568/thumb.png?ex=69420f46&is=6940bdc6&hm=fe01fd2b72afb98b26aaeb3090a6d29631923a98bb21151e6bbbd66f94323fad&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450307149472468992/thumb.png?ex=69420f49&is=6940bdc9&hm=4b640c20ba223e761725e31dccb2ef2684d407be8af6a1a8339fa1296b67a656&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450307162508361798/thumb.png?ex=69420f4c&is=6940bdcc&hm=f9049b04ef1565becb3a8642001f4419f8552ffdf5b90373f056924c80344db1&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450307184196980817/thumb.png?ex=69420f52&is=6940bdd2&hm=823b52bdc5653533c19a5de96955b609f38392ed3d30a85e8c9afe5e4e584c9a&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450307230816800912/thumb.png?ex=69420f5d&is=6940bddd&hm=e736d8f1025196002fa19ae4b23486c3829b51a276793aef64ca3dbce93ff382&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450307247224651967/thumb.png?ex=69420f61&is=6940bde1&hm=83b6e4d41d2ab4d8f0ab20deadce31efbb237cd8b86964242bc686ee91f31eb1&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450307265314947123/thumb.png?ex=69420f65&is=6940bde5&hm=79daf585e0d4682c8f4a604546a3cbed9a7642779764289e7a2aa6707a96240c&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450307283702648973/thumb.png?ex=69420f69&is=6940bde9&hm=02e054860f4a6d5c705eae06085f35aef546cf633ffd9c234d7bf81e1aced7f5&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450307322705350818/thumb.png?ex=69420f73&is=6940bdf3&hm=2284a83d8b88648199b776fcbee102379e708d761c8ba4f11298768f4bf06618&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450307335900758026/thumb.png?ex=69420f76&is=6940bdf6&hm=63da7f436c8755ebf0f0bbc7674090a0f481959d2b908a8af34827c1da6fdc9f&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450307346759811264/thumb.png?ex=69420f78&is=6940bdf8&hm=282609ba76c0858dcceeb89e8358899191341eeaacebbc617739e2358dd0c529&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450307353642536990/thumb.png?ex=69420f7a&is=6940bdfa&hm=4f89eb5a6571bd7ff95f95f67286f8be3f27a396b65f6efdca3d7c86175a0c48&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450307362060505229/thumb.png?ex=69420f7c&is=6940bdfc&hm=ca44cd8274c1f49568f905686112f1dadd1f98f532485b55447845f039dcef60&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450307445003129015/thumb.png?ex=69420f90&is=6940be10&hm=44e865bfb693ed0e6ddb31b8079d03ba38df5cc5196487a82c8956d6738991fb&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450307739002732705/thumb.png?ex=69420fd6&is=6940be56&hm=b4443cbc4446a2e2e86a3538278badb2e41496793feab6b3e7b3c7abf73be868&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450307752697270302/thumb.png?ex=69420fd9&is=6940be59&hm=5a650965dd67eeffa386c1586584ffe47e0410e17bd2022b11da8d5fba223b44&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450307769646452788/thumb.png?ex=69420fdd&is=6940be5d&hm=a85baf07413a2b7f50152266e223f32851741bf3ff4bbbb626a20f5190e5e4f3&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450307784485638305/thumb.png?ex=69420fe1&is=6940be61&hm=837ed23c1b8b5722e2400ccb35397e1354dab46a7c52ce830590d5b94e78240b&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450307816538505346/thumb.png?ex=69420fe8&is=6940be68&hm=b0fabc6beb00aef9b9810371366a18cac0ee746876d4028b09758c050f4919d9&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450307851611541547/thumb.png?ex=69420ff1&is=6940be71&hm=a9f26615e1806a5389506bd0f6a368c1303a1d45f5db38afb2a27c57f48232a8&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450307873543422095/thumb.png?ex=69420ff6&is=6940be76&hm=6db97f68d795ba1ddb5b3c3b35e0a133882657281032c3f76a03560e1ae94875&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450307892644413601/thumb.png?ex=69420ffb&is=6940be7b&hm=f37635659eb57e8ce74183b349766b12f82210edb213d904e43c89ff93cdaf56&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450307920494592072/thumb.png?ex=69421001&is=6940be81&hm=0bde0f31a92c0c601e9d307671ff0315c73169a23f959659f678721ccf78c92b&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450307932938965135/thumb.png?ex=69421004&is=6940be84&hm=760f92748ea2438afff0799638b677ffe6ade9a1de77ab1324f842261aebbab2&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450307944955645993/thumb.png?ex=69421007&is=6940be87&hm=9a776ddb507a48cb86710c9a3b4439b5e08416867de50f1a64e084da24fd6a50&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450307954900467802/thumb.png?ex=69421009&is=6940be89&hm=20bb78c91154d0ce7ece327c5e807a494081baa04705c81eeab975430dfe4312&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450307962450087956/thumb.png?ex=6942100b&is=6940be8b&hm=8382dd513d15eee3f436f67bc4db0296fbf1f0f29146ea46be37a0c848898e40&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450307969848840192/thumb.png?ex=6942100d&is=6940be8d&hm=dac4029098cf4a1b22b822f207d70e161fb997b4813109dad761af585c9d8fdf&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450308293947035778/thumb.png?ex=6942105a&is=6940beda&hm=59fc3c618cabd1ebe31c026872c892cd4cf17f85d3eb276825f83d5fd7e3c493&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450308306773082122/thumb.png?ex=6942105d&is=6940bedd&hm=8078bc0e12ab47aff09bedcfd2375903619d0918ca52a4d53cc11010bb575625&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450308323873390592/thumb.png?ex=69421061&is=6940bee1&hm=97867f64fe89be62c5514281c55e02bc5f8668bb4f9580ccffc6da2cb8411eab&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450308382685790218/thumb.png?ex=6942106f&is=6940beef&hm=ab8d1f80fce75ba5869d71ecaa651407b79edff71d34dec7f2bd5e652b404e6c&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450308399207153725/thumb.png?ex=69421073&is=6940bef3&hm=04fcd8883f0caba52e0cd98e6019af5c44074537884abb30131ea977296c93a6&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450308421340364810/thumb.png?ex=69421079&is=6940bef9&hm=43b917a998f6dbf2c1d501dda4942dbd3fbfc43b85f2efad3647152d56681b1d&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450308448351944785/thumb.png?ex=6942107f&is=6940beff&hm=c948b661aa88dbcc9936f8ae687647ff33785eeead01cd1ebaed675e52c4c8be&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450308472150425733/thumb.png?ex=69421085&is=6940bf05&hm=35b02a72d08e9dbc442502b982f8ea01551bb754ae99fd5bc034c4f6fd89db41&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450308490059976807/thumb.png?ex=69421089&is=6940bf09&hm=eb0f63b210c341da6b4ab59ae06c1ed5629b7e9c5f78bd636f5aea909bdcc805&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450308501841903646/thumb.png?ex=6942108c&is=6940bf0c&hm=bd1b3f8185ca77b30a097e692e984fe9264ba93425fe98e43b17928368ff5cc1&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450308514919747715/thumb.png?ex=6942108f&is=6940bf0f&hm=b9c4d4d144bc40622bab3e982272f20b23860decaca1360207e3299b7c2f5e23&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450308528362225764/thumb.png?ex=69421092&is=6940bf12&hm=1e8448b2fb4962bc7dc7ce0a378b475ca6e235fcaa92ead021d21924b02299e7&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450308553557409964/thumb.png?ex=69421098&is=6940bf18&hm=0555b4305fafac34fac5118250d5e7e9d803aefa07beb71d32ae886e42ca5b50&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450308561069674674/thumb.png?ex=6942109a&is=6940bf1a&hm=3ada957d2faaf0031dc5adece586a73b218d092c98b6b6d0587dd8364f576db3&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450308568291999979/thumb.png?ex=6942109c&is=6940bf1c&hm=d005e3daf61aad79585b631d11d99652764b0ec69114c03dd4b80685393721aa&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450309025186058240/thumb.png?ex=69421109&is=6940bf89&hm=646eeb6ddbe776eb6b05fe2a9b096fe2f772fc5a3ad563f57289595811664914&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450309040302456853/thumb.png?ex=6942110c&is=6940bf8c&hm=8fa68e8489340dc989c92659e0d2df7ac764c891758ca79757f804b1c14a80cd&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450309056484085882/thumb.png?ex=69421110&is=6940bf90&hm=d3e33a8d1d4864aa1b5e2a6a3ad7610308646695047f92b45c05744f6a469269&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450309073282007232/thumb.png?ex=69421114&is=6940bf94&hm=43e843f409ae8d6d3e0f87fc6d589a570237f8a337df77907e0bc512545f822c&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450309088696205333/thumb.png?ex=69421118&is=6940bf98&hm=b00f33215c2e28a29208b0f01f76315bd94bb7c539cdcf1e81f22130d88f6017&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450309105620357200/thumb.png?ex=6942111c&is=6940bf9c&hm=2a64447ff81f5e405f0e48ef58b8883a434ec00b32ac9ea18006287950c7bfd1&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450309131469848617/thumb.png?ex=69421122&is=6940bfa2&hm=23de2bcac4563a60128156413d8334c68869ad24a0a7a15d828f670e08639b19&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450309152722391050/thumb.png?ex=69421127&is=6940bfa7&hm=5ac388f602d0f467bf12b002fa9dd60476b885b9486326ef20e262ab189547bb&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450309169759518751/thumb.png?ex=6942112b&is=6940bfab&hm=b8d5dd339408ed8b14ccbcdad498045371e860b57e31639dcfbfe68544c1534f&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450309185852932287/thumb.png?ex=6942112f&is=6940bfaf&hm=185535f6879ab7a691557309430b6226dce3ff01d514bd8c08f40b53f3fde5fa&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450309203544510645/thumb.png?ex=69421133&is=6940bfb3&hm=54fa2013bef72d4e4dae37ff4a652702f6a087aeaa291af39efa40c2eb037e1a&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450309222884442229/thumb.png?ex=69421138&is=6940bfb8&hm=ee0bdd753c1471f8c6b3e8867ca79be90543b00b0c156961e00e64877cb87204&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450309274269122682/thumb.png?ex=69421144&is=6940bfc4&hm=82c911a3a503d5e65e240a597446b9c809ad468f139c1c8badab499dd96c3aa4&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450309287946621022/thumb.png?ex=69421147&is=6940bfc7&hm=aec3beb870865fd2eece070437c103609cf6cfaecb3eeed264448642b847f6da&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450309302848847882/thumb.png?ex=6942114b&is=6940bfcb&hm=fea08d120bc5e11b6b880e9da138dee85c741bdc46f18370678299eafab87177&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450309313594921044/thumb.png?ex=6942114d&is=6940bfcd&hm=e13ff5e12183f2e1bfb543691e5bd29f979736a662b79ed9a9e8933df03ac568&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450309323572908173/thumb.png?ex=69421150&is=6940bfd0&hm=f874cf389be4e07a80bbb9c935d64c80b1d345c574a542fceb8d375ea0524cc7&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450309329138876628/thumb.png?ex=69421151&is=6940bfd1&hm=e5ebcf30ae856441d6e957996aaf36ca92657d768b8c83f200bf8f9245b5f16b&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1450309337770627082/thumb.png?ex=69421153&is=6940bfd3&hm=1cf297f2f0723365bf9e0b0abbd5c4633231b75ac11068a13c74e108cd8f9279&",
    f"https://cdn.discordapp.com/attachments/1450304622806958103/1541493758334603415/thumb.png?ex=6a8dcb6f&is=6a8c79ef&hm=d1749bb0f2dd2c53074dd3d2e9053fb640a70e5d65b145c2f064eddfa41714b4&"
]
userScores = {}
raceScores = {}
index = -1
inRace = False
raceAmt = 0
startTime = time.time()
correct, incorrect, skips, hints = 0,0,0,0

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='u.', intents=intents)

@bot.event
async def on_ready():
    print(len(names))
    print(len(images))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)

@bot.command()
async def p(ctx, *, msg = ""):
    global index
    if msg == "":
        index = random.randint(0, 92)
        await ctx.send(f"here you go {images[index]}")
    if msg.lower() in names:
        await ctx.send(f"this is {names[names.index(msg.lower())]} \n {images[names.index(msg.lower())]}")

@bot.command()
async def h(ctx):
    if inRace:
        await ctx.send(f"there is an active race, you dont need to use the command to check, just type check")
    else:
        await ctx.send(f"the first letter is {names[index][0]}")

@bot.command()
async def c(ctx, *, msg):
    global index, userScores
    if index == -1:
        await ctx.send(f"there is no active id")
        return
    if inRace:
        await ctx.send(f"there is an active race, you dont need to use the command to check, just type the name")
        return
    if msg.lower() == names[index]:
        await ctx.send(f"{ctx.author.mention} is correct, that was {names[index]}")
        user = ctx.author.id
        if user in userScores:
            userScores.update({user: userScores[user]+1})
        else:
            userScores.update({user: 1})
        index = -1
        return
    if msg != names[index]:
        await ctx.send(f"incorrect, that was {names[index]}")
        index = -1

@bot.command()
async def s(ctx, *, msg = ""):
    if msg == "":
        if ctx.author.id in userScores:
            if userScores[ctx.author.id] > 1:
                await ctx.send(f"{ctx.author.mention} was correct {userScores[ctx.author.id]} times")
            else:
                await ctx.send(f"{ctx.author.mention} was correct 1 time")
        else:
            await ctx.send(f"{ctx.author.mention} has yet to answer correctly")
    else:
        name = msg
        name = name.replace("<", "")
        name = name.replace(">", "")
        name = name.replace("@", "")
        if int(name) in userScores:
            if userScores[int(name)] > 1:
                await ctx.send(f"{msg} was correct {userScores[int(name)]} times")
            else:
                await ctx.send(f"{msg} was correct 1 time")
        else:
            await ctx.send(f"{msg} has yet to answer correctly")

@bot.command()
async def i(ctx, *, msg):
    msg = msg.lower()
    if msg in names:
        index = names.index(msg)
        await ctx.send(f"this is {names[index]} \n {images[index]}")
    else:
        await ctx.send(f"not a valid name")

@bot.command()
async def test(ctx):
    return

@bot.command()
async def list(ctx):
    sortedlist = names.copy()
    sortedlist.sort()
    sentlist = "\n".join(sortedlist)
    await ctx.send(sentlist)

@bot.command()
async def goat(ctx):
    num = random.randint(0,3)
    if num == 0:
        await ctx.send("https://cdn.discordapp.com/attachments/1450304622806958103/1450308293947035778/thumb.png?ex=6942105a&is=6940beda&hm=59fc3c618cabd1ebe31c026872c892cd4cf17f85d3eb276825f83d5fd7e3c493&")
    if num == 1:
        await ctx.send("https://cdn.discordapp.com/attachments/1450304622806958103/1450309105620357200/thumb.png?ex=6942111c&is=6940bf9c&hm=2a64447ff81f5e405f0e48ef58b8883a434ec00b32ac9ea18006287950c7bfd1&")
    if num == 2:
        await ctx.send("https://cdn.discordapp.com/attachments/1450304622806958103/1450306592896450671/thumb.png?ex=69420ec5&is=6940bd45&hm=179eec4ee5bedd6ebd3d37c4bbbcadf0ced4823555f27f225057f7e6eb8a1fb3&")
    if num == 3:
        await ctx.send("https://cdn.discordapp.com/attachments/1450304622806958103/1450309185852932287/thumb.png?ex=6942112f&is=6940bfaf&hm=185535f6879ab7a691557309430b6226dce3ff01d514bd8c08f40b53f3fde5fa&")

@bot.command()
async def r(ctx, *, msg=""):
    global inRace, raceAmt, raceScores, index, startTime
    if len(msg) > 5:
        msg = msg.split()
        msg1 = msg[0]
        msg2 = msg[1]
        if msg1 == "start":
            if int(msg2) > 0:
                inRace = True
                raceAmt = int(msg2)
                startTime = time.time()
                await ctx.send(f"first to {raceAmt} correct ids wins")
                index = random.randint(0, 92)
                await ctx.send(f"here you go {images[index]}")
                return
    if str(msg) == "stop" and inRace:
        if bool(raceScores):
            winner = max(raceScores, key=lambda item:raceScores[item])
            await ctx.send(f"race stopped, <@{winner}> had the highest score of {raceScores[winner]}")
            inRace = False
            raceAmt = 0
            raceScores.clear()
        else:
            await ctx.send(f"race stopped")
    else:
        await ctx.send("input a valid number to start a race")

@bot.event
async def on_message(message):
    global index, raceAmt, userScores, raceScores, inRace, correct, incorrect, skips, hints
    if message.author == bot.user:
        return
    if inRace:
        if message.content.lower() in names:
            if message.content.lower() == names[index]:
                correct += 1
                await message.channel.send(f"{message.author.mention} is correct, that was {names[index]}")
                user = message.author.id
                if user in userScores:
                    userScores.update({user: userScores[user] + 1})
                else:
                    userScores.update({user: 1})
                if user in raceScores:
                    raceScores.update({user: raceScores[user] + 1})
                else:
                    raceScores.update({user: 1})
                if int(raceScores[user]) < raceAmt:
                    index = random.randint(0, 92)
                    await message.channel.send(f"here you go {images[index]}")
                else:
                    endTime = time.time()
                    await message.channel.send(f"{message.author.mention} has won the race in {int(endTime - startTime)} seconds \n total accuracy was {int(100*(correct/(correct+incorrect)))}% with {hints} hints and {skips} skips used")
                    raceScores.clear()
                    index = -1
                    inRace = False
                    raceAmt = 0
                    correct, incorrect, skips, hints = 0, 0, 0, 0
            else:
                await message.channel.send("incorrect")
                incorrect += 1
        if message.content.lower() == "skip":
            skips += 1
            await message.channel.send(f"skipping {names[index]}")
            index = random.randint(0, 92)
            await message.channel.send(f"here you go {images[index]}")
        if message.content.lower() == "hint":
            hints += 1
            await message.channel.send(f"the first letter is {names[index][0]}")
    await bot.process_commands(message)

bot.run(token, log_handler=handler, log_level=logging.DEBUG)