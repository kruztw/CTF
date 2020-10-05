#include <stdio.h>
#include <stdlib.h>
#include <string.h>

unsigned foo1(unsigned a1, unsigned a2) {
    unsigned v2 = 32 - a2;
    unsigned v3 = a1 << v2;
    unsigned v4 = a1 >> a2;
    unsigned current = v4 | v3;
    unsigned v5 = 32 - a2;
    unsigned v6 = a1 << v5;
    unsigned v7 = a1 >> a2;
    return current;
}

unsigned foo2(unsigned a1, unsigned a2) {
	unsigned v2 = 32 - a2;
	unsigned v3 = a1 >> v2;
	unsigned v4 = a1 << a2;
	unsigned current = v4 | v3;
	unsigned v5 = 32 - a2;
	unsigned v6 = a1 >> v5;
	unsigned v7 = a1 << a2;
	return current;
}

unsigned rands[] = {0, 0x77073096, 0x0EE0E612C, 0x990951BA, 0x76DC419, 0x706AF48F, 0x0E963A535, 0x9E6495A3, 0x0EDB8832, 0x79DCB8A4,
0x0E0D5E91E, 0x97D2D988, 0x9B64C2B,  0x7EB17CBD, 0x0E7B82D07, 0x90BF1D91, 0x1DB71064, 0x6AB020F2, 0x0F3B97148, 0x84BE41DE,
0x1ADAD47D, 0x6DDDE4EB, 0x0F4D4B551, 0x83D385C7, 0x136C9856, 0x646BA8C0, 0xFD62F97A, 0x8A65C9EC, 0x14015C4F, 0x63066CD9,
0x0FA0F3D63, 0x8D080DF5, 0x3B6E20C8, 0x4C69105E, 0x0D56041E4, 0x0A2677172, 0x3C03E4D1, 0x4B04D447, 0x0D20D85FD, 0x0A50AB56B,
0x35B5A8FA, 0x42B2986C, 0x0DBBBC9D6, 0x0ACBCF940, 0x32D86CE3, 0x45DF5C75, 0xDCD60DCF, 0x0ABD13D59, 0x26D930AC, 0x51DE003A, 0x0C8D75180, 0x0BFD06116,
 0x21B4F4B5, 0x56B3C423, 0x0CFBA9599, 0x0B8BDA50F, 0x5268E236, 0x2802B89E, 0x5F058808, 0x0C60CD9B2, 0x2F6F7C87, 0x58684C11, 0x0C1611DAB, 0x0B6662D3D, 0x76DC4190, 
 0x1DB7106, 0x98D220BC, 0x0EFD5102A, 0x71B18589, 0x6B6B51F, 0x9FBFE4A5, 0x0E8B8D433, 0x196C3671, 0x7807C9A2, 0x0F00F934, 0x9609A88E, 0x0E10E9818, 0x7F6A0DBB, 
 0x91646C97, 0x0E6635C01, 0x6B6B51F4, 0x1C6C6162, 0x0E5D5BE0D, 0x856530D8, 0x6C0695ED, 0x1B01A57B, 0x8208F4C1, 0x0F50FC457, 0x65B0D9C6, 0x12B7E950, 0x8BBEB8EA, 
 0x0FCB9887C, 0x62DD1DDF, 0x15DA2D49, 0x8CD37CF3, 0x0FBD44C65, 0x4DB26158, 0x3AB551CE, 0x0A3BC0074, 0x0D4BB30E2, 0x4ADFA541, 0x3DD895D7, 0x0A4D1C46D, 0x0D3D6F4FB,
 0x4369E96A, 0x346ED9FC, 0x0AD678846, 0x0DA60B8D0, 0x44042D73, 0x33031DE5, 0x0AA0A4C5F, 0x0DD0D7CC9, 0x5005713C, 0x270241AA, 0x0BE0B1010, 0x0C90C2086, 0x5768B525, 
 0x206F85B3, 0x0B966D409, 0x0CE61E49F, 0x29D9C998, 0x0B0D09822, 0x0C7D7A8B4, 0x59B33D17, 0x2EB40D81, 0x0B10BE924, 0x0B7BD5C3B, 0x0C0BA6CAD, 0x0EDB88320, 
 0x9ABFB3B6, 0x3B6E20C, 0x74B1D29A, 0x0EAD54739, 0x9DD277AF, 0x4DB2615, 0x73DC1683, 0x0E3630B12, 0x94643B84, 0x0D6D6A3E, 0x7A6A5AA8, 0x0E40ECF0B, 0x9309FF9D, 
 0x0A00AE27, 0x7D079EB1, 0x0F00F9344, 0x8708A3D2, 0x1E01F268, 0x6906C2FE, 0x0F762575D, 0x806567CB, 0x6E6B06E7, 0x0FED41B76, 0x89D32BE0, 0x10DA7A5A, 0x67DD4ACC,
 0x0F262004E, 0x0F9B9DF6F, 0x8EBEEFF9, 0x17B7BE43, 0x60B08ED5, 0x0D6D6A3E8, 0x0A1D1937E, 0x38D8C2C4, 0x4FDFF252, 0x0D1BB67F1, 0x0A6BC5767, 0x3FB506DD, 0x48B2364B,
 0x0D80D2BDA, 0x0AF0A1B4C, 0x36034AF6, 0x41047A60, 0x0DF60EFC3, 0x0A867DF55, 0x0CC0C7795, 0x0BB0B4703, 0x220216B9, 0x5505262F, 0x0C5BA3BBE, 0x0B2BD0B28, 
 0x316E8EEF, 0x4669BE79, 0x0CB61B38C, 0x5EDEF90E, 0x0BC66831A, 0x256FD2A0, 0x2BB45A92, 0x5CB36A04, 0x0C2D7FFA7, 0x0B5D0CF31, 0x2CD99E8B, 0x5BDEAE1D, 0x9B64C2B0, 
 0x0EC63F226, 0x756AA39C, 0x26D930A, 0x9C0906A9, 0x0EB0E363F, 0x72076785, 0x5005713, 0x95BF4A82, 0x0E2B87A14, 0x7BB12BAE, 0x0CB61B38, 0x92D28E9B, 0x7CDCEFB7, 
 0x0BDBDF21, 0x86D3D2D4, 0x0F1D4E242, 0x86D3D2D, 0x68DDB3F8, 0x1FDA836E, 0x81BE16CD, 0x0F6B9265B, 0x6FB077E1, 0x18B74777, 0x88085AE6, 0x0FF0F6A70, 0x66063BCA, 
 0x11010B5C, 0x8F659EFF, 0x0F862AE69, 0x616BFFD3, 0x166CCF45, 0x0A00AE278, 0x0D70DD2EE, 0x4E048354, 0x3903B3C2, 0x0A7672661, 0x0D06016F7, 0x4969474D, 0x3E6E77DB,
 0x0AED16A4A, 0x0D9D65ADC, 0x40DF0B66, 0x37D83BF0, 0x0A9BCAE53, 0x0DEBB9EC5, 0x47B2CF7F, 0x30B5FFE9, 0x0BDBDF21C, 0x0CABAC28A, 0x53B39330, 0x24B4A3A6, 0x0BAD03605,
 0x0CDD70693, 0x54DE5729, 0x23D967BF, 0x0B3667A2E, 0x0C4614AB8, 0x5D681B02, 0x2A6F2B94, 0x0B40BBE37, 0x0C30C8EA1, 0x5A05DF1B, 0x2D02EF8D};


unsigned start1[3] = {1, 2, 4};
unsigned start2[3] = {2, 0, 3};
unsigned start3[3] = {3, 5, 0};
unsigned rand2[3] = {0x7BA3E0DC, 0xE7F42D9A, 0xD9A4F450};
unsigned rand3[] = {0x9B3ECCA5, 0xEA10FB0, 0x5F18A534, 0xCEBCE886, 0xB8A0E16B, 0x8EBA9263};
unsigned rand4[] = {0xB30BB088, 0x60CCE52C, 0x8BB5A7C0, 0x3D4B4A14};

unsigned v4[4];
unsigned f[4];
unsigned current;
unsigned tmp0, tmp1, tmp2, tmp3, tmp4, tmp5, tmp6, tmp7, tmp8, tmp9, tmp10, tmp11, tmp12, tmp13, tmp14, tmp15, tmp16, tmp17;
unsigned tmp4s[6];

char flag[24] = "$C0PfU$c4ToR_1z_so_c00l!";   // tstlss{$C0PfU$c4ToR_1z_so_c00l!}

void addFlag() { // first round, we guess flag[1:3]

	flag[1] ++;
	if (flag[1] == 0x7f){
		flag[1] = 0x21;
		flag[2] += 1;
	}
	if (flag[2] == 0x7f){
		flag[2] = 0x21;
		flag[3] += 1;
	}
	return;
}

void load_tmp4s() {
	tmp4s[0] = tmp4;
	tmp4s[1] = tmp17;
	tmp4s[2] = tmp6;
	tmp4s[3] = tmp7;
	tmp4s[4] = tmp8;
	tmp4s[5] = tmp9;
}

void unload_tmp4s() {
	tmp4  = tmp4s[0];
	tmp17 = tmp4s[1];
	tmp6  = tmp4s[2];
	tmp7  = tmp4s[3];
	tmp8  = tmp4s[4];
	tmp9  = tmp4s[5];

}

int main() {

	// first round we guess flag[1:3], so initialize them first.
	flag[1] = flag[2] = flag[3] = '\x21';

	while (1) {

		int yes = 1;

		addFlag();
		printf("flag = %s\n", flag);

		tmp0 = ~0;
		for (int i = 0; i<3; ++i) { // i = 0; i<1; ++i
			unsigned offset1 = start1[i];
		    unsigned offset2 = start2[i];
		    unsigned offset3 = start3[i];

		    f[0] = flag[offset1];
		    f[1] = flag[offset2];
		    f[2] = flag[offset3];
		    f[3] = '\x00';

		    for (int j = 0; j<100; ++j) {
		        for (int k = 0; k<4; ++k) {
		        	tmp1 = current = tmp0 >> 8;
		            tmp2 = current = tmp0 ^ f[k];
		            tmp3 = current = tmp2 & 0xff;
		            tmp0 = current = rands[tmp3] ^ tmp1;
		        }
		    }

		    current = ~0;
		    tmp0 = current = tmp0 ^ current;
		    current = rand2[i];
		    if (tmp0 != current){
		    	printf("no\n");
		    	yes = 0;
		    	break;
		    }
		}

		/*
		if (yes) {
			printf("yes\n");
			break;
		}
		break;
		*/

		if (!yes)
			continue;

		current = 0xD3D6F4FB << 8;
		current = current | flag[6];
		tmp4 = current = foo1(current, 11);
		tmp5 = current = 0x6AB020F2 >> 8;
		current = flag[7] << 24;
		current = tmp5 | current;
		tmp17 = current = foo2(current, 23);
		tmp5 = current = 0xA9BCAE53 & 0xFFFF00FFLL;
		current = flag[8] << 8;
		current = tmp5 | current;
		tmp6 = foo1(current, 7);
		tmp5 = current = 0xF762575D & 0xFF00FFFFLL;
		current = flag[9] << 16;
		current = tmp5 | current;
		tmp7 = current = foo2(current, 19);
		current = ~flag[10];
		current = current & 0xff;
		tmp8 = current = foo1(rands[current], 5);
		current = ~rands[flag[11]];
		tmp9 = current = foo2(current, 27);


		for (int i = 0; i<10; ++i) {
			tmp5 = tmp4;
			load_tmp4s();
			for (unsigned j = 0; j<5; ++j) {
				tmp4s[j] = current = foo2(tmp4s[j+1], 11);
			}
			unload_tmp4s();
			tmp9 = current = foo2(tmp4, 11);
			load_tmp4s();
			for (int j = 0; j<6; ++j) {
				current = i<<3;
				tmp4s[j] = current = tmp4s[j] ^ rands[current];
			}
			unload_tmp4s();
		}

		for (int i = 5; i<6; ++i) {
			current = rand3[i];
			if (tmp4s[i] != current) {
				yes = 0;
				break;
			}
		}


		memmove(flag, &flag[12], 12);

		for (int i = 0; i<4; ++i) {
			tmp10 = current = 3*i;
			tmp11 = current = tmp10 + 2;
			tmp10 = current = 3*i;
			tmp12 = current = tmp10 + 1;
			tmp10 = current = 3*i;
			tmp13 = current = tmp10 + 0;
			tmp14 = current = flag[tmp12] << 8;
			tmp15 = current = flag[tmp13] << 16;
		    tmp16 = current = tmp15 | tmp14;
		    tmp16 = current = tmp16 | flag[tmp11];
		    tmp10 = current = tmp16 * 0x5BE794;
		    tmp14 = current = 2<<31;
		    tmp13 = current = tmp14 - 1;
		    tmp13 = current = tmp10 % tmp13;
		    v4[i] = current;
		}

		for (int i = 0; i<4; ++i) {
			if(v4[i] != rand4[i]){
				printf("no\n");
				yes = 0;
				break;
			}
		}

		if (yes) {
			printf("yes\n");
			break;
		}
	}
}