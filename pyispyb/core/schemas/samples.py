# import datetime

from typing import Optional
from pydantic import BaseModel, Field
from pyispyb.core import models

s = models.BLSample
c = models.Crystal
p = models.Protein


class ProteinBase(BaseModel):
    name: str
    acronym: str


class Protein(ProteinBase):
    proteinId: int

    class Config:
        orm_mode = True


class CrystalBase(BaseModel):
    cell_a: Optional[float] = Field(title="Cell A", nullable=True)
    cell_b: Optional[float] = Field(title="Cell B", nullable=True)
    cell_c: Optional[float] = Field(title="Cell C", nullable=True)
    cell_alpha: Optional[float] = Field(title="Cell Alpha", nullable=True)
    cell_beta: Optional[float] = Field(title="Cell Beta", nullable=True)
    cell_gamma: Optional[float] = Field(title="Cell Gamma", nullable=True)
    Protein: Protein


class Crystal(CrystalBase):
    crystalId: int

    Protein: Protein

    class Config:
        orm_mode = True


class SampleMetaData(BaseModel):
    subsamples: int = Field(description="Number of sub samples")
    datacollections: int = Field(description="Number of data collections")


class SampleBase(BaseModel):
    name: str
    comments: Optional[str] = Field(title="Comments", nullable=True)

    metadata: SampleMetaData = Field(alias="_metadata")


class Sample(SampleBase):
    blSampleId: int

    Crystal: Crystal

    class Config:
        orm_mode = True


# SELECT distinct b.blsampleid,
# b.crystalid,
# b.screencomponentgroupid,
# ssp.blsampleid as parentsampleid,
# ssp.name as parentsample,
# b.blsubsampleid,
# count(distinct si.blsampleimageid) as inspections,
# CONCAT(p.proposalcode,p.proposalnumber) as prop,
# b.code,
# b.location,
# pr.acronym,
# pr.proteinid,
# cr.spacegroup,b.comments,b.name,s.shippingname as shipment,s.shippingid,d.dewarid,d.code as dewar,
# c.code as container,
# c.containerid,
# c.samplechangerlocation as sclocation,
# count(distinct IF(dc.overlap != 0,dc.datacollectionid,NULL)) as sc,
# count(distinct IF(dc.overlap = 0 AND dc.axisrange = 0,dc.datacollectionid,NULL)) as gr,
# count(distinct IF(dc.overlap = 0 AND dc.axisrange > 0,dc.datacollectionid,NULL)) as dc,
# count(distinct IF(dcg.experimenttype LIKE 'XRF map',
# dc.datacollectionid,
# NULL)) as xm,
# count(distinct IF(dcg.experimenttype LIKE 'XRF spectrum',
# dc.datacollectionid,
# NULL)) as xs,
# count(distinct IF(dcg.experimenttype LIKE 'Energy scan',
# dc.datacollectionid,
# NULL)) as es,
# count(distinct so.screeningid) as ai,
# count(distinct app.autoprocprogramid) as ap,
# count(distinct r.robotactionid) as r,
# round(min(st.rankingresolution),2) as scresolution,
# max(ssw.completeness) as sccompleteness,
# round(min(apss.resolutionlimithigh),2) as dcresolution,
# round(max(apss.completeness),1) as dccompleteness,
# dp.anomalousscatterer,
# dp.requiredresolution,
# cr.cell_a,
# cr.cell_b,
# cr.cell_c,
# cr.cell_alpha,
# cr.cell_beta,
# cr.cell_gamma,
# b.packingfraction,
# b.dimension1,
# b.dimension2,
# b.dimension3,
# b.shape,
# cr.theoreticaldensity,
# cr.name as crystal,
# pr.name as protein,
# b.looptype,
# dp.centringmethod,
# dp.experimentkind,
# cq.containerqueueid,
# TO_CHAR(cq.createdtimestamp,
# 'DD-MM-YYYY HH24:MI') as queuedtimestamp
#                                   ,
# $cseq $sseq
# string_agg(cpr.name) as componentnames,
# string_agg(cpr.density) as componentdensities,
# tring_agg(cpr.proteinid) as componentids,
# string_agg(cpr.acronym) as componentacronyms,
# string_agg(cpr.global) as componentglobals,
# string_agg(chc.abundance) as componentamounts,
# string_agg(ct.symbol) as componenttypesymbols,
# b.volume,
# pct.symbol,ROUND(cr.abundance,3) as abundance,
# TO_CHAR(b.recordtimestamp,
# 'DD-MM-YYYY') as recordtimestamp,
# dp.radiationsensitivity,
# dp.energy,
# dp.userpath
