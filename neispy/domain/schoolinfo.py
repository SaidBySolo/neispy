from __future__ import annotations

from dataclasses import dataclass

from neispy.domain.abc import NeisObject, SchoolRelated
from neispy.types.schoolinfo import SchoolInfoDict
from neispy.utils import Deserializer


@dataclass
class SchoolInfoRow(SchoolRelated):
    ENG_SCHUL_NM: str
    """영문학교명"""
    SCHUL_KND_SC_NM: str
    """학교종류명"""
    LCTN_SC_NM: str
    """소재지명"""
    JU_ORG_NM: str
    """관할조직명"""
    FOND_SC_NM: str
    """설립명"""
    ORG_RDNZC: str
    """도로명우편번호"""
    ORG_RDNMA: str
    """도로명주소"""
    ORG_RDNDA: str
    """도로명상세주소"""
    ORG_TELNO: str
    """전화번호"""
    HMPG_ADRES: str
    """홈페이지주소"""
    COEDU_SC_NM: str
    """남녀공학구분명"""
    ORG_FAXNO: str
    """팩스번호"""
    HS_SC_NM: str
    """고등학교구분명"""
    INDST_SPECL_CCCCL_EXST_YN: str
    """산업체특별학급존재여부"""
    HS_GNRL_BUSNS_SC_NM: str
    """고등학교일반실업구분명"""
    SPCLY_PURPS_HS_ORD_NM: str
    """특수목적고등학교계열명"""
    ENE_BFE_SEHF_SC_NM: str
    """입시전후기구분명"""
    DGHT_SC_NM: str
    """주야구분명"""
    FOND_YMD: str
    """설립일자"""
    FOAS_MEMRD: str
    """개교기념일"""
    LOAD_DTM: str
    """수정일"""


@dataclass
class SchoolInfo(Deserializer):
    schoolInfo: NeisObject[SchoolInfoRow]

    @classmethod
    def from_dict(cls, d: SchoolInfoDict) -> SchoolInfo:
        return super().from_dict(d)
