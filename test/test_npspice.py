from wrapper.ngspice import NGSpice
from os import getcwd
from asyncio import run


def test_ngspice():
    sim = NGSpice(sim_path="C:/Users/Manouda/PycharmProjects/fastAPI/simulators/Spice64/bin/ngspice_con.exe")
    run(sim.run(f"{getcwd()}/test/schem_test.net", f"{getcwd()}/test/"))

    assert len(sim.results.keys()) == 6
