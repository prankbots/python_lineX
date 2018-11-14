# AUTO KICK 12 AKUN.
# KALO SCRIPTNYA KLIATAN RAPIH PASTI SCRIPTNYA JUGA BAGUS
# LU BELI BARANG JUGA PASTI NYARINYA YANG GAK ACAK ACAKAN.
# DAN ITU PASTI LU PILIH YANG KUALITASNYA BAGUS JUGA YE KAN.
# INTINYA KALO SCRIPTNYA TERLIHAT RAPI DAH PASTI BIKINYA JUGA GAK ASAL ASALAN.
"""
AUTHOR
Creator by : acil
Bot name : auto kicker v.12.1.0
Repository : http://github.com/Aprank
System : python 3.6 or python 3.5
Thrift : thrift==0.11.0
Libs : Line_X_prankBots
Country :: INDONESIA. Hacking LINE :D
"""
from LINE_X import *
from datetime import datetime, timedelta
from time import sleep
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess
team_prankBots = ["uedf09eaa64df4ab3dbc2365d3b356236"]
#TOKET BUNDA#

#TEAM 1
auto_kick_v1 = LINE("TOKEN")
auto_kick_v2 = LINE("TOKEN")
auto_kick_v3 = LINE("TOKEN")
auto_kick_v4 = LINE("TOKEN")
#TEAM 2
auto_kick_v5 = LINE("TOKEN")
auto_kick_v6 = LINE("TOKEN")
auto_kick_v7 = LINE("TOKEN")
auto_kick_v8 = LINE("TOKEN")
#TEAM 3
auto_kick_v9 = LINE("TOKEN")
auto_kick_v10 = LINE("TOKEN")
auto_kick_v11 = LINE("TOKEN")
auto_kick_v12 = LINE("TOKEN")

#VARTIBLE
Line_XprankBot = OEPoll(auto_kick_v1)
Java_auto_kick_v1 = auto_kick_v1.profile.mid
Java_auto_kick_v2 = auto_kick_v2.profile.mid
Java_auto_kick_v3 = auto_kick_v3.profile.mid
Java_auto_kick_v4 = auto_kick_v4.profile.mid
Java_auto_kick_v5 = auto_kick_v5.profile.mid
Java_auto_kick_v6 = auto_kick_v6.profile.mid
Java_auto_kick_v7 = auto_kick_v7.profile.mid
Java_auto_kick_v8 = auto_kick_v8.profile.mid
Java_auto_kick_v9 = auto_kick_v9.profile.mid
Java_auto_kick_v10 = auto_kick_v10.profile.mid
Java_auto_kick_v11 = auto_kick_v11.profile.mid
Java_auto_kick_v12 = auto_kick_v12.profile.mid
Connect_bot_v1 = [Java_auto_kick_v1,Java_auto_kick_v2,Java_auto_kick_v3,Java_auto_kick_v4]
Connect_bot_v2 = [Java_auto_kick_v5,Java_auto_kick_v6,Java_auto_kick_v7,Java_auto_kick_v8]
Connect_bot_v3 = [Java_auto_kick_v9,Java_auto_kick_v10,Java_auto_kick_v11,Java_auto_kick_v12]
Connect_bot_start = Connect_bot_v1+Connect_bot_v2+Connect_bot_v3+team_prankBots
Primare_v1 = [auto_kick_v1,auto_kick_v2,auto_kick_v3,auto_kick_v4]
Primare_v2 = [auto_kick_v5,auto_kick_v6,auto_kick_v7,auto_kick_v8]
Primare_v3 = [auto_kick_v9,auto_kick_v10,auto_kick_v11,auto_kick_v12]
Server_home = {"autokick": False, "service_home": "0.0.0.0"}
Block_Id = {
    "Block_Id": {}
}
""" parser """
responseinBot = "Already.."
reasonSucces = "Success.."
reasonNone = "Noting.!"
def responversion1():
  msg = op.message
  Porwar = msg.to
  auto_kick_v1.sendMessage(Porwar, "Already on")
def responversion2():
  msg = op.message
  Porwar = msg.to
  auto_kick_v1.sendMessage(Porwar, "Already off")
def responversion3():
  msg = op.message
  Porwar = msg.to
  auto_kick_v1.sendMessage(Porwar, "restarting..")
def responversion_id1():
  msg = op.message
  Porwar = msg.to
  auto_kick_v1.sendMessage(Porwar, reasonNone)
  auto_kick_v2.sendMessage(Porwar, reasonNone)
  auto_kick_v3.sendMessage(Porwar, reasonNone)
  auto_kick_v4.sendMessage(Porwar, reasonNone)
  auto_kick_v5.sendMessage(Porwar, reasonNone)
  auto_kick_v6.sendMessage(Porwar, reasonNone)
  auto_kick_v7.sendMessage(Porwar, reasonNone)
  auto_kick_v8.sendMessage(Porwar, reasonNone)
  auto_kick_v9.sendMessage(Porwar, reasonNone)
  auto_kick_v10.sendMessage(Porwar, reasonNone)
  auto_kick_v11.sendMessage(Porwar, reasonNone)
  auto_kick_v12.sendMessage(Porwar, reasonNone)
def responversion_id():
  msg = op.message
  Porwar = msg.to
  auto_kick_v1.sendMessage(Porwar, "Waiting prosses.!!")
def Cresponversion_id1():
  msg = op.message
  Porwar = msg.to
  auto_kick_v1.sendMessage(Porwar, reasonSucces)
  auto_kick_v2.sendMessage(Porwar, reasonSucces)
  auto_kick_v3.sendMessage(Porwar, reasonSucces)
  auto_kick_v4.sendMessage(Porwar, reasonSucces)
  auto_kick_v5.sendMessage(Porwar, reasonSucces)
  auto_kick_v6.sendMessage(Porwar, reasonSucces)
  auto_kick_v7.sendMessage(Porwar, reasonSucces)
  auto_kick_v8.sendMessage(Porwar, reasonSucces)
  auto_kick_v9.sendMessage(Porwar, reasonSucces)
  auto_kick_v10.sendMessage(Porwar, reasonSucces)
  auto_kick_v11.sendMessage(Porwar, reasonSucces)
  auto_kick_v12.sendMessage(Porwar, reasonSucces)
def responversion_in1():
  msg = op.message
  Porwar = msg.to
  auto_kick_v1.sendMessage(Porwar, responseinBot)
  auto_kick_v2.sendMessage(Porwar, responseinBot)
  auto_kick_v3.sendMessage(Porwar, responseinBot)
  auto_kick_v4.sendMessage(Porwar, responseinBot)
  auto_kick_v5.sendMessage(Porwar, responseinBot)
  auto_kick_v6.sendMessage(Porwar, responseinBot)
  auto_kick_v7.sendMessage(Porwar, responseinBot)
  auto_kick_v8.sendMessage(Porwar, responseinBot)
  auto_kick_v9.sendMessage(Porwar, responseinBot)
  auto_kick_v10.sendMessage(Porwar, responseinBot)
  auto_kick_v11.sendMessage(Porwar, responseinBot)
  auto_kick_v12.sendMessage(Porwar, responseinBot)
def inparserBot():
  Frank = auto_kick_v1.getGroup(to)
  Frank.preventedJoinByTicket = False
  auto_kick_v1.updateGroup(Frank)
  invsend = 0
  Tracklink = auto_kick_v1.reissueGroupTicket(to)
  auto_kick_v1.acceptGroupInvitationByTicket(to, Tracklink)
  auto_kick_v2.acceptGroupInvitationByTicket(to, Tracklink)
  auto_kick_v3.acceptGroupInvitationByTicket(to, Tracklink)
  auto_kick_v4.acceptGroupInvitationByTicket(to, Tracklink)
  auto_kick_v5.acceptGroupInvitationByTicket(to, Tracklink)
  auto_kick_v6.acceptGroupInvitationByTicket(to, Tracklink)
  auto_kick_v7.acceptGroupInvitationByTicket(to, Tracklink)
  auto_kick_v8.acceptGroupInvitationByTicket(to, Tracklink)
  auto_kick_v9.acceptGroupInvitationByTicket(to, Tracklink)
  auto_kick_v10.acceptGroupInvitationByTicket(to, Tracklink)
  auto_kick_v11.acceptGroupInvitationByTicket(to, Tracklink)
  auto_kick_v12.acceptGroupInvitationByTicket(to, Tracklink)
  Frank.preventedJoinByTicket = True
  auto_kick_v1.updateGroup(Frank)
def outparserBot():
  Frank = auto_kick_v1.getGroup(to)
  auto_kick_v12.leaveGroup(Frank)
  auto_kick_v11.leaveGroup(Frank)
  auto_kick_v10.leaveGroup(Frank)
  auto_kick_v9.leaveGroup(Frank)
  auto_kick_v8.leaveGroup(Frank)
  auto_kick_v7.leaveGroup(Frank)
  auto_kick_v6.leaveGroup(Frank)
  auto_kick_v5.leaveGroup(Frank)
  auto_kick_v4.leaveGroup(Frank)
  auto_kick_v3.leaveGroup(Frank)
  auto_kick_v2.leaveGroup(Frank)
  auto_kick_v1.leaveGroup(Frank)
def prank_bot(op):
  try:
    if op.type == 0:
      return
    if op.type == 15:
      black_of_gamer = op.param1
      girl_of_gamer = op.param2
      line_x_tride = op.param3
      if girl_of_gamer in Java_auto_kick_v1:
        auto_kick_v2.leaveGroup(black_of_gamer)
        auto_kick_v3.leaveGroup(black_of_gamer)
        auto_kick_v4.leaveGroup(black_of_gamer)
        auto_kick_v5.leaveGroup(black_of_gamer)
        auto_kick_v6.leaveGroup(black_of_gamer)
        auto_kick_v7.leaveGroup(black_of_gamer)
        auto_kick_v8.leaveGroup(black_of_gamer)
        auto_kick_v9.leaveGroup(black_of_gamer)
        auto_kick_v10.leaveGroup(black_of_gamer)
        auto_kick_v11.leaveGroup(black_of_gamer)
        auto_kick_v12.leaveGroup(black_of_gamer)
    if op.type == 13:
      black_of_gamer = op.param1
      girl_of_gamer = op.param2
      line_x_tride = op.param3
      if Java_auto_kick_v1 in line_x_tride:
        if girl_of_gamer in team_prankBots:
          auto_kick_v1.acceptGroupInvitation(black_of_gamer)
          auto_kick_v2.acceptGroupInvitation(black_of_gamer)
          auto_kick_v3.acceptGroupInvitation(black_of_gamer)
          auto_kick_v4.acceptGroupInvitation(black_of_gamer)
          auto_kick_v5.acceptGroupInvitation(black_of_gamer)
          auto_kick_v6.acceptGroupInvitation(black_of_gamer)
          auto_kick_v7.acceptGroupInvitation(black_of_gamer)
          auto_kick_v8.acceptGroupInvitation(black_of_gamer)
          auto_kick_v9.acceptGroupInvitation(black_of_gamer)
          auto_kick_v10.acceptGroupInvitation(black_of_gamer)
          auto_kick_v11.acceptGroupInvitation(black_of_gamer)
          auto_kick_v12.acceptGroupInvitation(black_of_gamer)
        else:
          auto_kick_v1.acceptGroupInvitation(black_of_gamer)
          auto_kick_v1.sendMessage(black_of_gamer,"don't invite me thanks.!")
          auto_kick_v1.leaveGroup(black_of_gamer)
      if Java_auto_kick_v2 in line_x_tride:
        if girl_of_gamer in team_prankBots:
          auto_kick_v2.acceptGroupInvitation(black_of_gamer)
        else:
          auto_kick_v2.acceptGroupInvitation(black_of_gamer)
          auto_kick_v2.leaveGroup(black_of_gamer)
      if Java_auto_kick_v3 in line_x_tride:
        if girl_of_gamer in team_prankBots:
          auto_kick_v3.acceptGroupInvitation(black_of_gamer)
        else:
          auto_kick_v3.acceptGroupInvitation(black_of_gamer)
          auto_kick_v3.leaveGroup(black_of_gamer)
      if Java_auto_kick_v4 in line_x_tride:
        if girl_of_gamer in team_prankBots:
          auto_kick_v4.acceptGroupInvitation(black_of_gamer)
        else:
          auto_kick_v4.acceptGroupInvitation(black_of_gamer)
          auto_kick_v4.leaveGroup(black_of_gamer)
      if Java_auto_kick_v5 in line_x_tride:
        if girl_of_gamer in team_prankBots:
          auto_kick_v5.acceptGroupInvitation(black_of_gamer)
        else:
          auto_kick_v5.acceptGroupInvitation(black_of_gamer)
          auto_kick_v5.leaveGroup(black_of_gamer)
      if Java_auto_kick_v6 in line_x_tride:
        if girl_of_gamer in team_prankBots:
          auto_kick_v6.acceptGroupInvitation(black_of_gamer)
        else:
          auto_kick_v6.acceptGroupInvitation(black_of_gamer)
          auto_kick_v6.leaveGroup(black_of_gamer)
      if Java_auto_kick_v7 in line_x_tride:
        if girl_of_gamer in team_prankBots:
          auto_kick_v7.acceptGroupInvitation(black_of_gamer)
        else:
          auto_kick_v7.acceptGroupInvitation(black_of_gamer)
          auto_kick_v7.leaveGroup(black_of_gamer)
      if Java_auto_kick_v8 in line_x_tride:
        if girl_of_gamer in team_prankBots:
          auto_kick_v8.acceptGroupInvitation(black_of_gamer)
        else:
          auto_kick_v8.acceptGroupInvitation(black_of_gamer)
          auto_kick_v8.leaveGroup(black_of_gamer)
      if Java_auto_kick_v9 in line_x_tride:
        if girl_of_gamer in team_prankBots:
          auto_kick_v9.acceptGroupInvitation(black_of_gamer)
        else:
          auto_kick_v9.acceptGroupInvitation(black_of_gamer)
          auto_kick_v9.leaveGroup(black_of_gamer)
      if Java_auto_kick_v10 in line_x_tride:
        if girl_of_gamer in team_prankBots:
          auto_kick_v10.acceptGroupInvitation(black_of_gamer)
        else:
          auto_kick_v10.acceptGroupInvitation(black_of_gamer)
          auto_kick_v10.leaveGroup(black_of_gamer)
      if Java_auto_kick_v11 in line_x_tride:
        if girl_of_gamer in team_prankBots:
          auto_kick_v11.acceptGroupInvitation(black_of_gamer)
        else:
          auto_kick_v11.acceptGroupInvitation(black_of_gamer)
          auto_kick_v11.leaveGroup(black_of_gamer)
      if Java_auto_kick_v12 in line_x_tride:
        if girl_of_gamer in team_prankBots:
          auto_kick_v12.acceptGroupInvitation(black_of_gamer)
        else:
          auto_kick_v12.acceptGroupInvitation(black_of_gamer)
          auto_kick_v12.leaveGroup(black_of_gamer)
    if op.type == 13:
      black_of_gamer = op.param1
      girl_of_gamer = auto_kick_v1.getContact(op.param2)
      if set["autokick"] == True:
        auto_kick_v1.acceptGroupInvitation(black_of_gamer)
        team_one = auto_kick_v1.getGroup(black_of_gamer)
        team_one.preventedJoinByTicket = False
        auto_kick_v1.updateGroup(team_one)
        Tracklist = auto_kick_v1.reissueGroupTicket(black_of_gamer)
        auto_kick_v2.acceptGroupInvitationByTicket(black_of_gamer,Tracklist)
        auto_kick_v3.acceptGroupInvitationByTicket(black_of_gamer,Tracklist)
        auto_kick_v4.acceptGroupInvitationByTicket(black_of_gamer,Tracklist)
        auto_kick_v5.acceptGroupInvitationByTicket(black_of_gamer,Tracklist)
        auto_kick_v6.acceptGroupInvitationByTicket(black_of_gamer,Tracklist)
        auto_kick_v7.acceptGroupInvitationByTicket(black_of_gamer,Tracklist)
        auto_kick_v8.acceptGroupInvitationByTicket(black_of_gamer,Tracklist)
        auto_kick_v9.acceptGroupInvitationByTicket(black_of_gamer,Tracklist)
        auto_kick_v10.acceptGroupInvitationByTicket(black_of_gamer,Tracklist)
        auto_kick_v11.acceptGroupInvitationByTicket(black_of_gamer,Tracklist)
        auto_kick_v12.acceptGroupInvitationByTicket(black_of_gamer,Tracklist)
        for target in auto_kick_v1.getGroup(black_of_gamer).members:
          extaktor = target.mid
          if not target in Connect_bot_start:
            try:
              kick_Start_1 = random.choice(Primare_v1)
              kick_Start_1.kickoutFromGroup(black_of_gamer,[extaktor])
              print ("Team 1 Start kick in group\nMember Name : "+target.displayName)
            except:
              try:
                kick_Start_2 = random.choice(Primare_v2)
                kick_Start_2.kickoutFromGroup(black_of_gamer,[extaktor])
                print ("Team 2 Start kick in group\nMember Name : "+target.displayName)
              except:
                kick_Start_3 = random.choice(Primare_v3)
                kick_Start_3.kickoutFromGroup(black_of_gamer,[extaktor])
                print ("Team 3 Start kick in group\nMember Name : "+target.displayName)
        else:
          xtrime_proses = []
          for xtrime_start in auto_kick_v1.getGroup(black_of_gamer).members:
            xtrime_proses.append(xtrime_start.mid)
            if xtrime_proses == []:
              auto_kick_v1.sendMessage(black_of_gamer,"limit.!")
            else:
              for start_kick in xtrime_proses:
                if not start_kick in Connect_bot_start:
                  try:
                    kick_Start_1 = random.choice(Primare_v1)
                    kick_Start_1.kickoutFromGroup(black_of_gamer,[start_kick])
                    print ("Team 1 Start kick in group\nMember Name : "+xtrime_start.displayName)
                  except:
                    try:
                      kick_Start_2 = random.choice(Primare_v2)
                      kick_Start_2.kickoutFromGroup(black_of_gamer,[start_kick])
                      print ("Team 2 Start kick in group\nMember Name : "+xtrime_start.displayName)
                    except:
                      kick_Start_3 = random.choice(Primare_v3)
                      kick_Start_3.kickoutFromGroup(black_of_gamer,[start_kick])
                      print ("Team 3 Start kick in group\nMember Name : "+xtrime_start.displayName)
    if op.type == 19 or op.type == 32:
      black_of_gamer = op.param1
      girl_of_gamer = op.param2
      line_x_tride = op.param3
      kick_Start_1 = random.choice(Primare_v1)
      kick_Start_2 = random.choice(Primare_v2)
      kick_Start_3 = random.choice(Primare_v3)
      if line_x_tride in Connect_bot_v1:
        if girl_of_gamer in Connect_bot_start:
          pass
        else:
          Block_Id["Block_Id"][girl_of_gamer] = True
          try:
            team_one = kick_Start_2.getGroup(black_of_gamer)
            team_one.preventedJoinByTicket = False
            kick_Start_2.updateGroup(team_one)
            Tracklist = kick_Start_2.reissueGroupTicket(black_of_gamer)
            kick_Start_2.kickoutFromGroup(black_of_gamer,[girl_of_gamer])
            auto_kick_v1.acceptGroupInvitationByTicket(black_of_gamer,Tracklist)
            auto_kick_v2.acceptGroupInvitationByTicket(black_of_gamer,Tracklist)
            auto_kick_v3.acceptGroupInvitationByTicket(black_of_gamer,Tracklist)
            auto_kick_v4.acceptGroupInvitationByTicket(black_of_gamer,Tracklist)
            print ("Team 1 masuk kembali")
          except:pass
      if line_x_tride in Connect_bot_v2:
        if girl_of_gamer in Connect_bot_start:
          pass
        else:
          Block_Id["Block_Id"][girl_of_gamer] = True
          try:
            team_one = kick_Start_3.getGroup(black_of_gamer)
            team_one.preventedJoinByTicket = False
            kick_Start_3.updateGroup(team_one)
            Tracklist = kick_Start_3.reissueGroupTicket(black_of_gamer)
            kick_Start_3.kickoutFromGroup(black_of_gamer,[girl_of_gamer])
            auto_kick_v5.acceptGroupInvitationByTicket(black_of_gamer,Tracklist)
            auto_kick_v6.acceptGroupInvitationByTicket(black_of_gamer,Tracklist)
            auto_kick_v7.acceptGroupInvitationByTicket(black_of_gamer,Tracklist)
            auto_kick_v8.acceptGroupInvitationByTicket(black_of_gamer,Tracklist)
            print ("Team 2 masuk kembali")
          except:pass
      if line_x_tride in Connect_bot_v3:
        if girl_of_gamer in Connect_bot_start:
          pass
        else:
          Block_Id["Block_Id"][girl_of_gamer] = True
          try:
            team_one = kick_Start_1.getGroup(black_of_gamer)
            team_one.preventedJoinByTicket = False
            kick_Start_1.updateGroup(team_one)
            Tracklist = kick_Start_1.reissueGroupTicket(black_of_gamer)
            kick_Start_1.kickoutFromGroup(black_of_gamer,[girl_of_gamer])
            auto_kick_v9.acceptGroupInvitationByTicket(black_of_gamer,Tracklist)
            auto_kick_v10.acceptGroupInvitationByTicket(black_of_gamer,Tracklist)
            auto_kick_v11.acceptGroupInvitationByTicket(black_of_gamer,Tracklist)
            auto_kick_v12.acceptGroupInvitationByTicket(black_of_gamer,Tracklist)
            print ("Team 1 masuk kembali")
          except:pass
    if op.type == 25 or op.type == 26:
      msg = op.message
      text = msg.text
      Porwar = msg.to
      From = msg._from
      if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
        if msg.toType == 0:
          if From != auto_kick_v1.profile.mid:
            to = From
          else:
            to = Porwar
        elif msg.toType == 1:
          to = Porwar
        elif msg.toType == 2:
          to = Porwar
        if msg.contentType == 0:
          if text is None:
            return
          else:
              LineX = text.lower()
              if LineX == "autokick:on" and From == team_prankBots:
                Server_home["autokick"] = True
                responversion1()
              if LineX == "autokick:off" and From == team_prankBots:
                Server_home["autokick"] = False
                responversion2()
              if LineX == "restart" and From == team_prankBots:
                Server_home["service_home"] = Porwar
                responversion3()
                python = sys.executable
                os.execl(python, python, *sys.argv)
              if LineX == "banlist" and From == team_prankBots:
                if Block_Id["Block_Id"] == {}:
                  responversion_id1()
                else:
                  responversion_id()
                  exceptions = ""
                  for breack in Block_Id["Block_Id"]:
                    exceptions = auto_kick_v1.getContact(breack)
                    auto_kick_v1.sendContact(Porwar,breack)
              if LineX == "clearban" and From == team_prankBots:
                Block_Id["Block_Id"] = {}
                Cresponversion_id1()
              if LineX == "respon" and From == team_prankBots:
                responversion_in1()
              if LineX == "out" and From == team_prankBots:
                outparserBot()
              if LineX == "in" and From == team_prankBots:
                inparserBot()
  except Exception as Broken_python:
    auto_kick_v1.log(str(Broken_python))
    """
    buatlah sebuah program ini dalam logs
    akan berfungsi untuk mengetahui sys
    pada saat system berbahaya atau err.
    PRANKBOTS CREATOR.
    """
    if op.type == 59:
      print (op)
      """
      while true ini system dari semua paryabel di atas
      anda tidak bisa menghilangkan ini.
      semua system akan rusak dan tidak berfungsi
      PRANKBOTS CREATOR
      """
while True:
  try:
    ops=Line_XprankBot.singleTrace(count=50)
    if ops != None:
      for op in ops: 
        prank_bot(op)
        Line_XprankBot.setRevision(op.revision)
  except Exception as Broken_python:
    auto_kick_v1.log(str(Broken_python))
"""
AUTHOR
Creator by : acil
Bot name : auto kicker v.12.1.0
Repository : http://github.com/Aprank
System : python 3.6 or python 3.5
Thrift : thrift==0.11.0
Libs : Line_X_prankBots
Country :: INDONESIA. Hacking LINE :D
"""
