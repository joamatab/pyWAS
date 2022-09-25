"""
Base class for spice simulator
"""
from abc import ABC, abstractmethod
from pydantic import BaseModel, FilePath, DirectoryPath
from enum import Enum
from typing import List, Optional
from asyncio import StreamReader
from parse.results import ResultDict


class SupportedSimulator(str, Enum):
    ngsice = "ngspice"


class SimulatorType(str, Enum):
    spice = "spice"
    em = "em"


class SimulationType(str, Enum):
    ac = "ac"
    dc = "dc"
    tran = "tran"


class SpiceWrapper(BaseModel, ABC):
    name: SupportedSimulator
    path: FilePath
    supported_sim: List[SimulationType]
    results: Optional[ResultDict]

    def add_to_queue(self):
        """
        Not Implemented Yet.
        :return:
        """

    @abstractmethod
    async def run(self, _spice_file: FilePath, log_folder: DirectoryPath):
        """
        run the spice simulation describe by the _spice_file
        :param _spice_file: spice file to be simulated
        :param log_folder: directory to write simulation log
        :return: a temp file of the raw out of the simulator (to be process by serialize_result)
        """

    @abstractmethod
    async def parse_out(self, stream: StreamReader):
        """
            Convert simulation output to ResultDict
        :return:
        """

    @abstractmethod
    async def parse_err(self, stream: StreamReader):
        """
            Capture error and print it
        :return:
        """
