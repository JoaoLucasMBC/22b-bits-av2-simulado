#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""


from myhdl import *
from ula_aux import *


def exe1(a, b, c, q):
    @always_comb
    def comb():
        q.next = (a & b) | ((b & c) & (b | c))

    return instances()


def exe2(p, q, r, s):
    @always_comb
    def comb():
        s.next = (q and r) or (not p)

    return instances()


def exe3(x1, x0, y1, y0, z3, z2, z1, z0):
    @always_comb
    def comb():
        z0.next = 0
        z1.next = 0
        z2.next = 0
        z3.next = 0

    return instances()


def exe4_ula(a, b, inverte_a, inverte_b, c_in, c_out, selecao, zero, resultado):
    negA = Signal(modbv(0)[32:])
    negB = Signal(modbv(0)[32:])
    
    muxA_out = Signal(modbv(0)[32:])
    muxB_out = Signal(modbv(0)[32:])
    mux4_out = Signal(modbv(0)[32:])

    add_out = Signal(modbv(0)[32:])
    and_out = Signal(modbv(0)[32:])
    or_out = Signal(modbv(0)[32:])

    zerado = Signal(modbv(0)[32:])

    muxA = mux2way(muxA_out, a, negA, inverte_a)

    muxB = mux2way(muxB_out, b, negB, inverte_b)

    addAB = adder(add_out, c_out, muxA_out, muxB_out, c_in)

    mux4 = mux4way(mux4_out, and_out, or_out, add_out, zerado, selecao)
    
    @always_comb
    def comb():
        negA.next = not a
        negB.next = not b

        and_out.next = muxA_out and muxB_out
        or_out.next = muxA_out or muxB_out

        resultado.next = mux4_out
        zero.next = not(mux4_out or mux4_out)

    return instances()