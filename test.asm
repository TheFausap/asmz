; A174864 (OEIS)
ROUND   .bss    10
MAXR    .set    10
		cla
		loa	1
		adi
		loa 1
		ldir0
		loa MAXR
		ldir1
lab1	incr0
		jgt	end
		lor2
		adi
		lor2
		adi
		cpyr2
		lor0
		mui
		stpr
		outp
		jmp	lab1
end		hlt