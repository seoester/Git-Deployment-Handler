# -*- coding: utf-8 -*-

from gitdh.modules import Module
from gitdh import gitdhutils

class DatabaseLog(Module):
	def isEnabled(self, action):
		return (action == "postreceive" and "Database" in self.config)

	def preProcessing(self, commits):
		for commit in commits:
			if "DatabaseLog" in self.config[commit.branch] and self.config.getboolean(commit.branch, "DatabaseLog"):
				commit.status = "databaselog_queued"

	def processing(self, commits):
		commits = gitdhutils.filterOnStatusBase("databaselog", commits)
		gitdhutils.mInsertCommit(self.dbBe, commits)
