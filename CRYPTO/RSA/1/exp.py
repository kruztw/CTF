import gmpy2
from pwn import *

N = 6146024643941503757217715363256725297474582575057128830681803952150464985329239705861504172069973746764596350359462277397739134788481500502387716062571912861345331755396960400668616401300689786263797654804338789112750913548642482662809784602704174564885963722422299918304645125966515910080631257020529794610856299507980828520629245187681653190311198219403188372517508164871722474627810848320169613689716990022730088459821267951447201867517626158744944551445617408339432658443496118067189012595726036261168251749186085493288311314941584653172141498507582033165337666796171940245572657593635107816849481870784366174740265906662098222589242955869775789843661127411493630943226776741646463845546396213149027737171200372484413863565567390083316799725434855960709541328144058411807356607316377373917707720258565704707770352508576366053160404360862976120784192082599228536166245480722359263166146184992593735550019325337524138545418186493193366973466749752806880403086988489013389009843734224502284325825989
c = 3572030904528013180691184031825875018560018830056027446538585108046374607199842488138228426133620939067295245642162497675548656988031367698701161407333098336631469820625758165691216722102954230039803062571915807926805842311530808555825502457067483266045370081698397234434007948071948000301674260889742505705689105049976374758307610890478956315615270346544731420764623411884522772647227485422185741972880247913540403503772495257290866993158120540920089734332219140638231258380844037266185237491107152677366121632644100162619601924591268704611229987050199163281293994502948372872259033482851597923104208041748275169138684724529347356731689014177146308752441720676090362823472528200449780703866597108548404590800249980122989260948630061847682889941399385098680402067366390334436739269305750501804725143228482932118740926602413362231953728010397307348540059759689560081517028515279382023371274623802620886821099991568528927696544505357451279263250695311793770159474896431625763008081110926072287874375257
e = 65537

for carry in range(100):
    x = (int(str(N)[:250]) - carry )*(10**250) + int(str(N)[-250:])
    y = (N - x*(10**500) - x) / (10**250)

    a_b, ok = gmpy2.iroot(2*x+y, 2)
    if ok:
        p_q = a_b * (10**250) + a_b
        phi = N - p_q + 1
        d = gmpy2.invert(e, phi)

        m = pow(c, d, N)
        print unhex(hex(m)[2:])

