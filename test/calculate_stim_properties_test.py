#    Copyright (C) <2019>  <Tamás Zolnai>  <zolnaitamas2000@gmail.com>

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

#!\\usr\\bin\\env python
# -*- coding: utf-8 -*-

import unittest

import os

import sys
# Add the local path to the main script so we can import it.
sys.path = [".."] + sys.path

import asrt

class calculateStimpropertiesTest(unittest.TestCase):

    def testImplicitASRT(self):
        experiment = asrt.Experiment("")
        experiment.settings = asrt.ExperimentSettings("", "")
        experiment.settings.epochN = 10
        experiment.settings.epochs = [5, 5]
        experiment.settings.block_in_epochN = 5
        experiment.settings.blockprepN = 5
        experiment.settings.blocklengthN = 80
        experiment.settings.asrt_rcolor = "Orange"
        experiment.settings.asrt_pcolor = "Green"
        experiment.settings.asrt_types = {}
        experiment.settings.asrt_types[1] = "implicit"
        experiment.settings.asrt_types[2] = "implicit"

        experiment.stim_sessionN = {}
        experiment.end_at = {}
        experiment.stimepoch = {}
        experiment.stimblock = {}
        experiment.stimtrial = {}
        experiment.stimlist = {}
        experiment.stim_colorN = {}
        experiment.stimpr = {}
        experiment.PCodes = {}
        experiment.PCodes [1] = "1st - 1234"
        experiment.PCodes [2] = "1st - 1234"
        experiment.calculate_stim_properties()

        self.assertEqual(len(experiment.stim_sessionN), experiment.settings.get_maxtrial())
        self.assertEqual(len(experiment.end_at), experiment.settings.get_maxtrial())
        self.assertEqual(len(experiment.stimepoch), experiment.settings.get_maxtrial())
        self.assertEqual(len(experiment.stimblock), experiment.settings.get_maxtrial())
        self.assertEqual(len(experiment.stimtrial), experiment.settings.get_maxtrial())
        self.assertEqual(len(experiment.stimlist), experiment.settings.get_maxtrial())
        self.assertEqual(len(experiment.stim_colorN), experiment.settings.get_maxtrial())
        self.assertEqual(len(experiment.stimpr), experiment.settings.get_maxtrial())

        for i in range(len(experiment.stim_sessionN)):
            if i < experiment.settings.get_maxtrial() / 2:
                self.assertEqual(experiment.stim_sessionN[i+1], 1)
            else:
                self.assertEqual(experiment.stim_sessionN[i+1], 2)

        for i in range(len(experiment.end_at)):
            if i < experiment.settings.get_maxtrial() / 2:
                self.assertEqual(experiment.end_at[i+1], experiment.settings.get_maxtrial() / 2 + 1)
            else:
                self.assertEqual(experiment.end_at[i+1], experiment.settings.get_maxtrial() + 1)

        for i in range(len(experiment.stimepoch)):
            self.assertEqual(experiment.stimepoch[i+1], i // ((experiment.settings.blockprepN+experiment.settings.blocklengthN)*experiment.settings.block_in_epochN) + 1)

        for i in range(len(experiment.stimblock)):
            self.assertEqual(experiment.stimblock[i+1], i // (experiment.settings.blockprepN+experiment.settings.blocklengthN) + 1)

        for i in range(len(experiment.stimtrial)):
            self.assertEqual(experiment.stimtrial[i+1], i % (experiment.settings.blockprepN+experiment.settings.blocklengthN) + 1)

        count_1 = 0
        count_2 = 0
        count_3 = 0
        oount_4 = 0
        for i in range(len(experiment.stimlist)):
            trial_num_in_block = i % (experiment.settings.blockprepN+experiment.settings.blocklengthN) + 1
            if trial_num_in_block > experiment.settings.blockprepN and (trial_num_in_block - experiment.settings.blockprepN) % 2 == 1:
                if experiment.stimlist[i+1] == 1:
                    count_1 += 1
                elif experiment.stimlist[i+1] == 2:
                    count_2 += 1
                elif experiment.stimlist[i+1] == 3:
                    count_3 += 1
                elif experiment.stimlist[i+1] == 4:
                    oount_4 += 1

        self.assertEqual(count_1, 500)
        self.assertEqual(count_2, 500)
        self.assertEqual(count_3, 500)
        self.assertEqual(oount_4, 500)

        # implicit asrt
        for i in range(len(experiment.stim_colorN)):
            self.assertEqual(experiment.stim_colorN[i+1], "Orange")

        for i in range(len(experiment.stimpr)):
            trial_num_in_block = i % (experiment.settings.blockprepN+experiment.settings.blocklengthN) + 1
            if trial_num_in_block > experiment.settings.blockprepN and (trial_num_in_block - experiment.settings.blockprepN) % 2 == 1:
                self.assertEqual(experiment.stimpr[i+1], "P")
            else:
                self.assertEqual(experiment.stimpr[i+1], "R")

    def testExplicitASRT(self):
        experiment = asrt.Experiment("")
        experiment.settings = asrt.ExperimentSettings("", "")
        experiment.settings.epochN = 10
        experiment.settings.epochs = [5, 5]
        experiment.settings.block_in_epochN = 5
        experiment.settings.blockprepN = 5
        experiment.settings.blocklengthN = 80
        experiment.settings.asrt_rcolor = "Orange"
        experiment.settings.asrt_pcolor = "Green"
        experiment.settings.asrt_types = {}
        experiment.settings.asrt_types[1] = "explicit"
        experiment.settings.asrt_types[2] = "explicit"

        experiment.stim_sessionN = {}
        experiment.end_at = {}
        experiment.stimepoch = {}
        experiment.stimblock = {}
        experiment.stimtrial = {}
        experiment.stimlist = {}
        experiment.stim_colorN = {}
        experiment.stimpr = {}
        experiment.PCodes = {}
        experiment.PCodes [1] = "2nd - 1243"
        experiment.PCodes [2] = "3rd - 1324"
        experiment.calculate_stim_properties()

        self.assertEqual(len(experiment.stim_sessionN), experiment.settings.get_maxtrial())
        self.assertEqual(len(experiment.end_at), experiment.settings.get_maxtrial())
        self.assertEqual(len(experiment.stimepoch), experiment.settings.get_maxtrial())
        self.assertEqual(len(experiment.stimblock), experiment.settings.get_maxtrial())
        self.assertEqual(len(experiment.stimtrial), experiment.settings.get_maxtrial())
        self.assertEqual(len(experiment.stimlist), experiment.settings.get_maxtrial())
        self.assertEqual(len(experiment.stim_colorN), experiment.settings.get_maxtrial())
        self.assertEqual(len(experiment.stimpr), experiment.settings.get_maxtrial())

        for i in range(len(experiment.stim_sessionN)):
            if i < experiment.settings.get_maxtrial() / 2:
                self.assertEqual(experiment.stim_sessionN[i+1], 1)
            else:
                self.assertEqual(experiment.stim_sessionN[i+1], 2)

        for i in range(len(experiment.end_at)):
            if i < experiment.settings.get_maxtrial() / 2:
                self.assertEqual(experiment.end_at[i+1], experiment.settings.get_maxtrial() / 2 + 1)
            else:
                self.assertEqual(experiment.end_at[i+1], experiment.settings.get_maxtrial() + 1)

        for i in range(len(experiment.stimepoch)):
            self.assertEqual(experiment.stimepoch[i+1], i // ((experiment.settings.blockprepN+experiment.settings.blocklengthN)*experiment.settings.block_in_epochN) + 1)

        for i in range(len(experiment.stimblock)):
            self.assertEqual(experiment.stimblock[i+1], i // (experiment.settings.blockprepN+experiment.settings.blocklengthN) + 1)

        for i in range(len(experiment.stimtrial)):
            self.assertEqual(experiment.stimtrial[i+1], i % (experiment.settings.blockprepN+experiment.settings.blocklengthN) + 1)

        count_1 = 0
        count_2 = 0
        count_3 = 0
        oount_4 = 0
        for i in range(len(experiment.stimlist)):
            trial_num_in_block = i % (experiment.settings.blockprepN+experiment.settings.blocklengthN) + 1
            if trial_num_in_block > experiment.settings.blockprepN and (trial_num_in_block - experiment.settings.blockprepN) % 2 == 1:
                if experiment.stimlist[i+1] == 1:
                    count_1 += 1
                elif experiment.stimlist[i+1] == 2:
                    count_2 += 1
                elif experiment.stimlist[i+1] == 3:
                    count_3 += 1
                elif experiment.stimlist[i+1] == 4:
                    oount_4 += 1

        self.assertEqual(count_1, 500)
        self.assertEqual(count_2, 500)
        self.assertEqual(count_3, 500)
        self.assertEqual(oount_4, 500)

        # implicit asrt
        for i in range(len(experiment.stim_colorN)):
            trial_num_in_block = i % (experiment.settings.blockprepN+experiment.settings.blocklengthN) + 1
            if trial_num_in_block > experiment.settings.blockprepN and (trial_num_in_block - experiment.settings.blockprepN) % 2 == 1:
                self.assertEqual(experiment.stim_colorN[i+1], "Green")
            else:
                self.assertEqual(experiment.stim_colorN[i+1], "Orange")

        for i in range(len(experiment.stimpr)):
            trial_num_in_block = i % (experiment.settings.blockprepN+experiment.settings.blocklengthN) + 1
            if trial_num_in_block > experiment.settings.blockprepN and (trial_num_in_block - experiment.settings.blockprepN) % 2 == 1:
                self.assertEqual(experiment.stimpr[i+1], "P")
            else:
                self.assertEqual(experiment.stimpr[i+1], "R")

    def testNoASRT(self):
        experiment = asrt.Experiment("")
        experiment.settings = asrt.ExperimentSettings("", "")
        experiment.settings.epochN = 5
        experiment.settings.epochs = [5]
        experiment.settings.block_in_epochN = 5
        experiment.settings.blockprepN = 5
        experiment.settings.blocklengthN = 80
        experiment.settings.asrt_rcolor = "Orange"
        experiment.settings.asrt_pcolor = "Green"
        experiment.settings.asrt_types = {}
        experiment.settings.asrt_types[1] = "noASRT"

        experiment.stim_sessionN = {}
        experiment.end_at = {}
        experiment.stimepoch = {}
        experiment.stimblock = {}
        experiment.stimtrial = {}
        experiment.stimlist = {}
        experiment.stim_colorN = {}
        experiment.stimpr = {}
        experiment.PCodes = {}
        experiment.PCodes [1] = "noPattern"
        experiment.calculate_stim_properties()

        self.assertEqual(len(experiment.stim_sessionN), experiment.settings.get_maxtrial())
        self.assertEqual(len(experiment.end_at), experiment.settings.get_maxtrial())
        self.assertEqual(len(experiment.stimepoch), experiment.settings.get_maxtrial())
        self.assertEqual(len(experiment.stimblock), experiment.settings.get_maxtrial())
        self.assertEqual(len(experiment.stimtrial), experiment.settings.get_maxtrial())
        self.assertEqual(len(experiment.stimlist), experiment.settings.get_maxtrial())
        self.assertEqual(len(experiment.stim_colorN), experiment.settings.get_maxtrial())
        self.assertEqual(len(experiment.stimpr), experiment.settings.get_maxtrial())

        # all trials are in the same session
        for i in range(len(experiment.stim_sessionN)):
            self.assertEqual(experiment.stim_sessionN[i+1], 1)

        for i in range(len(experiment.end_at)):
            self.assertEqual(experiment.end_at[i+1], experiment.settings.get_maxtrial() + 1)

        for i in range(len(experiment.stimepoch)):
            self.assertEqual(experiment.stimepoch[i+1], i // ((experiment.settings.blockprepN+experiment.settings.blocklengthN)*experiment.settings.block_in_epochN) + 1)

        for i in range(len(experiment.stimblock)):
            self.assertEqual(experiment.stimblock[i+1], i // (experiment.settings.blockprepN+experiment.settings.blocklengthN) + 1)

        for i in range(len(experiment.stimtrial)):
            self.assertEqual(experiment.stimtrial[i+1], i % (experiment.settings.blockprepN+experiment.settings.blocklengthN) + 1)

        count_1 = 0
        count_2 = 0
        count_3 = 0
        oount_4 = 0
        for i in range(len(experiment.stimlist)):
            trial_num_in_block = i % (experiment.settings.blockprepN+experiment.settings.blocklengthN) + 1
            if trial_num_in_block > experiment.settings.blockprepN and (trial_num_in_block - experiment.settings.blockprepN) % 2 == 1:
                if experiment.stimlist[i+1] == 1:
                    count_1 += 1
                elif experiment.stimlist[i+1] == 2:
                    count_2 += 1
                elif experiment.stimlist[i+1] == 3:
                    count_3 += 1
                elif experiment.stimlist[i+1] == 4:
                    oount_4 += 1

        # randomized data
        self.assertTrue(count_1 != count_2)
        self.assertTrue(count_3 != oount_4)

        # implicit asrt
        for i in range(len(experiment.stim_colorN)):
            self.assertEqual(experiment.stim_colorN[i+1], "Orange")

        for i in range(len(experiment.stimpr)):
            self.assertEqual(experiment.stimpr[i+1], "R")

    def testASRTWithoutPractice(self):
        experiment = asrt.Experiment("")
        experiment.settings = asrt.ExperimentSettings("", "")
        experiment.settings.epochN = 5
        experiment.settings.epochs = [5]
        experiment.settings.block_in_epochN = 5
        experiment.settings.blockprepN = 0
        experiment.settings.blocklengthN = 80
        experiment.settings.asrt_rcolor = "Orange"
        experiment.settings.asrt_pcolor = "Green"
        experiment.settings.asrt_types = {}
        experiment.settings.asrt_types[1] = "implicit"

        experiment.stim_sessionN = {}
        experiment.end_at = {}
        experiment.stimepoch = {}
        experiment.stimblock = {}
        experiment.stimtrial = {}
        experiment.stimlist = {}
        experiment.stim_colorN = {}
        experiment.stimpr = {}
        experiment.PCodes = {}
        experiment.PCodes [1] = "1st - 1234"
        experiment.calculate_stim_properties()

        self.assertEqual(len(experiment.stim_sessionN), experiment.settings.get_maxtrial())
        self.assertEqual(len(experiment.end_at), experiment.settings.get_maxtrial())
        self.assertEqual(len(experiment.stimepoch), experiment.settings.get_maxtrial())
        self.assertEqual(len(experiment.stimblock), experiment.settings.get_maxtrial())
        self.assertEqual(len(experiment.stimtrial), experiment.settings.get_maxtrial())
        self.assertEqual(len(experiment.stimlist), experiment.settings.get_maxtrial())
        self.assertEqual(len(experiment.stim_colorN), experiment.settings.get_maxtrial())
        self.assertEqual(len(experiment.stimpr), experiment.settings.get_maxtrial())

        # all trials are in the same session
        for i in range(len(experiment.stim_sessionN)):
            self.assertEqual(experiment.stim_sessionN[i+1], 1)

        for i in range(len(experiment.end_at)):
            self.assertEqual(experiment.end_at[i+1], experiment.settings.get_maxtrial() + 1)

        for i in range(len(experiment.stimepoch)):
            self.assertEqual(experiment.stimepoch[i+1], i // ((experiment.settings.blockprepN+experiment.settings.blocklengthN)*experiment.settings.block_in_epochN) + 1)

        for i in range(len(experiment.stimblock)):
            self.assertEqual(experiment.stimblock[i+1], i // (experiment.settings.blockprepN+experiment.settings.blocklengthN) + 1)

        for i in range(len(experiment.stimtrial)):
            self.assertEqual(experiment.stimtrial[i+1], i % (experiment.settings.blockprepN+experiment.settings.blocklengthN) + 1)

        count_1 = 0
        count_2 = 0
        count_3 = 0
        oount_4 = 0
        for i in range(len(experiment.stimlist)):
            trial_num_in_block = i % (experiment.settings.blockprepN+experiment.settings.blocklengthN) + 1
            if trial_num_in_block > experiment.settings.blockprepN and (trial_num_in_block - experiment.settings.blockprepN) % 2 == 1:
                if experiment.stimlist[i+1] == 1:
                    count_1 += 1
                elif experiment.stimlist[i+1] == 2:
                    count_2 += 1
                elif experiment.stimlist[i+1] == 3:
                    count_3 += 1
                elif experiment.stimlist[i+1] == 4:
                    oount_4 += 1

        self.assertEqual(count_1, 250)
        self.assertEqual(count_2, 250)
        self.assertEqual(count_3, 250)
        self.assertEqual(oount_4, 250)

        # implicit asrt
        for i in range(len(experiment.stim_colorN)):
            self.assertEqual(experiment.stim_colorN[i+1], "Orange")

        for i in range(len(experiment.stimpr)):
            trial_num_in_block = i % (experiment.settings.blockprepN+experiment.settings.blocklengthN) + 1
            if trial_num_in_block > experiment.settings.blockprepN and (trial_num_in_block - experiment.settings.blockprepN) % 2 == 1:
                self.assertEqual(experiment.stimpr[i+1], "P")
            else:
                self.assertEqual(experiment.stimpr[i+1], "R")

    def testASRTWithoutReal(self):
        experiment = asrt.Experiment("")
        experiment.settings = asrt.ExperimentSettings("", "")
        experiment.settings.epochN = 5
        experiment.settings.epochs = [5]
        experiment.settings.block_in_epochN = 5
        experiment.settings.blockprepN = 5
        experiment.settings.blocklengthN = 0
        experiment.settings.asrt_rcolor = "Orange"
        experiment.settings.asrt_pcolor = "Green"
        experiment.settings.asrt_types = {}
        experiment.settings.asrt_types[1] = "implicit"

        experiment.stim_sessionN = {}
        experiment.end_at = {}
        experiment.stimepoch = {}
        experiment.stimblock = {}
        experiment.stimtrial = {}
        experiment.stimlist = {}
        experiment.stim_colorN = {}
        experiment.stimpr = {}
        experiment.PCodes = {}
        experiment.PCodes [1] = "1st - 1234"
        experiment.calculate_stim_properties()

        self.assertEqual(len(experiment.stim_sessionN), experiment.settings.get_maxtrial())
        self.assertEqual(len(experiment.end_at), experiment.settings.get_maxtrial())
        self.assertEqual(len(experiment.stimepoch), experiment.settings.get_maxtrial())
        self.assertEqual(len(experiment.stimblock), experiment.settings.get_maxtrial())
        self.assertEqual(len(experiment.stimtrial), experiment.settings.get_maxtrial())
        self.assertEqual(len(experiment.stimlist), experiment.settings.get_maxtrial())
        self.assertEqual(len(experiment.stim_colorN), experiment.settings.get_maxtrial())
        self.assertEqual(len(experiment.stimpr), experiment.settings.get_maxtrial())

        # all trials are in the same session
        for i in range(len(experiment.stim_sessionN)):
            self.assertEqual(experiment.stim_sessionN[i+1], 1)

        for i in range(len(experiment.end_at)):
            self.assertEqual(experiment.end_at[i+1], experiment.settings.get_maxtrial() + 1)

        for i in range(len(experiment.stimepoch)):
            self.assertEqual(experiment.stimepoch[i+1], i // ((experiment.settings.blockprepN+experiment.settings.blocklengthN)*experiment.settings.block_in_epochN) + 1)

        for i in range(len(experiment.stimblock)):
            self.assertEqual(experiment.stimblock[i+1], i // (experiment.settings.blockprepN+experiment.settings.blocklengthN) + 1)

        for i in range(len(experiment.stimtrial)):
            self.assertEqual(experiment.stimtrial[i+1], i % (experiment.settings.blockprepN+experiment.settings.blocklengthN) + 1)

        # random only
        for i in range(len(experiment.stim_colorN)):
            self.assertEqual(experiment.stim_colorN[i+1], "Orange")

        # random only
        for i in range(len(experiment.stimpr)):
            self.assertEqual(experiment.stimpr[i+1], "R")

    def testWithEvenPracticeTrials(self):
        experiment = asrt.Experiment("")
        experiment.settings = asrt.ExperimentSettings("", "")
        experiment.settings.epochN = 5
        experiment.settings.epochs = [5]
        experiment.settings.block_in_epochN = 5
        experiment.settings.blockprepN = 6
        experiment.settings.blocklengthN = 80
        experiment.settings.asrt_rcolor = "Orange"
        experiment.settings.asrt_pcolor = "Green"
        experiment.settings.asrt_types = {}
        experiment.settings.asrt_types[1] = "implicit"

        experiment.stim_sessionN = {}
        experiment.end_at = {}
        experiment.stimepoch = {}
        experiment.stimblock = {}
        experiment.stimtrial = {}
        experiment.stimlist = {}
        experiment.stim_colorN = {}
        experiment.stimpr = {}
        experiment.PCodes = {}
        experiment.PCodes [1] = "1st - 1234"
        experiment.calculate_stim_properties()

        self.assertEqual(len(experiment.stim_sessionN), experiment.settings.get_maxtrial())
        self.assertEqual(len(experiment.end_at), experiment.settings.get_maxtrial())
        self.assertEqual(len(experiment.stimepoch), experiment.settings.get_maxtrial())
        self.assertEqual(len(experiment.stimblock), experiment.settings.get_maxtrial())
        self.assertEqual(len(experiment.stimtrial), experiment.settings.get_maxtrial())
        self.assertEqual(len(experiment.stimlist), experiment.settings.get_maxtrial())
        self.assertEqual(len(experiment.stim_colorN), experiment.settings.get_maxtrial())
        self.assertEqual(len(experiment.stimpr), experiment.settings.get_maxtrial())

        # all trials are in the same session
        for i in range(len(experiment.stim_sessionN)):
            self.assertEqual(experiment.stim_sessionN[i+1], 1)

        for i in range(len(experiment.end_at)):
            self.assertEqual(experiment.end_at[i+1], experiment.settings.get_maxtrial() + 1)

        for i in range(len(experiment.stimepoch)):
            self.assertEqual(experiment.stimepoch[i+1], i // ((experiment.settings.blockprepN+experiment.settings.blocklengthN)*experiment.settings.block_in_epochN) + 1)

        for i in range(len(experiment.stimblock)):
            self.assertEqual(experiment.stimblock[i+1], i // (experiment.settings.blockprepN+experiment.settings.blocklengthN) + 1)

        for i in range(len(experiment.stimtrial)):
            self.assertEqual(experiment.stimtrial[i+1], i % (experiment.settings.blockprepN+experiment.settings.blocklengthN) + 1)

        count_1 = 0
        count_2 = 0
        count_3 = 0
        oount_4 = 0
        for i in range(len(experiment.stimlist)):
            trial_num_in_block = i % (experiment.settings.blockprepN+experiment.settings.blocklengthN) + 1
            if trial_num_in_block > experiment.settings.blockprepN and (trial_num_in_block - experiment.settings.blockprepN) % 2 == 1:
                if experiment.stimlist[i+1] == 1:
                    count_1 += 1
                elif experiment.stimlist[i+1] == 2:
                    count_2 += 1
                elif experiment.stimlist[i+1] == 3:
                    count_3 += 1
                elif experiment.stimlist[i+1] == 4:
                    oount_4 += 1

        self.assertEqual(count_1, 250)
        self.assertEqual(count_2, 250)
        self.assertEqual(count_3, 250)
        self.assertEqual(oount_4, 250)

        # implicit asrt
        for i in range(len(experiment.stim_colorN)):
            self.assertEqual(experiment.stim_colorN[i+1], "Orange")

        for i in range(len(experiment.stimpr)):
            trial_num_in_block = i % (experiment.settings.blockprepN+experiment.settings.blocklengthN) + 1
            if trial_num_in_block > experiment.settings.blockprepN and (trial_num_in_block - experiment.settings.blockprepN) % 2 == 1:
                self.assertEqual(experiment.stimpr[i+1], "P")
            else:
                self.assertEqual(experiment.stimpr[i+1], "R")

    def testWithOddRealTrials(self):
        experiment = asrt.Experiment("")
        experiment.settings = asrt.ExperimentSettings("", "")
        experiment.settings.epochN = 5
        experiment.settings.epochs = [5]
        experiment.settings.block_in_epochN = 5
        experiment.settings.blockprepN = 6
        experiment.settings.blocklengthN = 75
        experiment.settings.asrt_rcolor = "Orange"
        experiment.settings.asrt_pcolor = "Green"
        experiment.settings.asrt_types = {}
        experiment.settings.asrt_types[1] = "implicit"

        experiment.stim_sessionN = {}
        experiment.end_at = {}
        experiment.stimepoch = {}
        experiment.stimblock = {}
        experiment.stimtrial = {}
        experiment.stimlist = {}
        experiment.stim_colorN = {}
        experiment.stimpr = {}
        experiment.PCodes = {}
        experiment.PCodes [1] = "1st - 1234"
        experiment.calculate_stim_properties()

        self.assertEqual(len(experiment.stim_sessionN), experiment.settings.get_maxtrial())
        self.assertEqual(len(experiment.end_at), experiment.settings.get_maxtrial())
        self.assertEqual(len(experiment.stimepoch), experiment.settings.get_maxtrial())
        self.assertEqual(len(experiment.stimblock), experiment.settings.get_maxtrial())
        self.assertEqual(len(experiment.stimtrial), experiment.settings.get_maxtrial())
        self.assertEqual(len(experiment.stimlist), experiment.settings.get_maxtrial())
        self.assertEqual(len(experiment.stim_colorN), experiment.settings.get_maxtrial())
        self.assertEqual(len(experiment.stimpr), experiment.settings.get_maxtrial())

        # all trials are in the same session
        for i in range(len(experiment.stim_sessionN)):
            self.assertEqual(experiment.stim_sessionN[i+1], 1)

        for i in range(len(experiment.end_at)):
            self.assertEqual(experiment.end_at[i+1], experiment.settings.get_maxtrial() + 1)

        for i in range(len(experiment.stimepoch)):
            self.assertEqual(experiment.stimepoch[i+1], i // ((experiment.settings.blockprepN+experiment.settings.blocklengthN)*experiment.settings.block_in_epochN) + 1)

        for i in range(len(experiment.stimblock)):
            self.assertEqual(experiment.stimblock[i+1], i // (experiment.settings.blockprepN+experiment.settings.blocklengthN) + 1)

        for i in range(len(experiment.stimtrial)):
            self.assertEqual(experiment.stimtrial[i+1], i % (experiment.settings.blockprepN+experiment.settings.blocklengthN) + 1)

        count_1 = 0
        count_2 = 0
        count_3 = 0
        oount_4 = 0
        for i in range(len(experiment.stimlist)):
            trial_num_in_block = i % (experiment.settings.blockprepN+experiment.settings.blocklengthN) + 1
            if trial_num_in_block > experiment.settings.blockprepN and (trial_num_in_block - experiment.settings.blockprepN) % 2 == 1:
                if experiment.stimlist[i+1] == 1:
                    count_1 += 1
                elif experiment.stimlist[i+1] == 2:
                    count_2 += 1
                elif experiment.stimlist[i+1] == 3:
                    count_3 += 1
                elif experiment.stimlist[i+1] == 4:
                    oount_4 += 1

        # there are some variance in the number, becuase some pattern trials are cut down at the end of the blocks
        self.assertAlmostEqual(count_1, 237, delta=5)
        self.assertAlmostEqual(count_2, 237, delta=5)
        self.assertAlmostEqual(count_3, 237, delta=5)
        self.assertAlmostEqual(oount_4, 237, delta=5)

        # implicit asrt
        for i in range(len(experiment.stim_colorN)):
            self.assertEqual(experiment.stim_colorN[i+1], "Orange")

        for i in range(len(experiment.stimpr)):
            trial_num_in_block = i % (experiment.settings.blockprepN+experiment.settings.blocklengthN) + 1
            if trial_num_in_block > experiment.settings.blockprepN and (trial_num_in_block - experiment.settings.blockprepN) % 2 == 1:
                self.assertEqual(experiment.stimpr[i+1], "P")
            else:
                self.assertEqual(experiment.stimpr[i+1], "R")

    def testMoreSessionsWithDifferentProperties(self):
        experiment = asrt.Experiment("")
        experiment.settings = asrt.ExperimentSettings("", "")
        experiment.settings.epochN = 10
        experiment.settings.epochs = [2, 5, 4]
        experiment.settings.block_in_epochN = 5
        experiment.settings.blockprepN = 5
        experiment.settings.blocklengthN = 80
        experiment.settings.asrt_rcolor = "Orange"
        experiment.settings.asrt_pcolor = "Green"
        experiment.settings.asrt_types = {}
        experiment.settings.asrt_types[1] = "explicit"
        experiment.settings.asrt_types[2] = "implicit"
        experiment.settings.asrt_types[3] = "noASRT"

        experiment.stim_sessionN = {}
        experiment.end_at = {}
        experiment.stimepoch = {}
        experiment.stimblock = {}
        experiment.stimtrial = {}
        experiment.stimlist = {}
        experiment.stim_colorN = {}
        experiment.stimpr = {}
        experiment.PCodes = {}
        experiment.PCodes [1] = "2nd - 1243"
        experiment.PCodes [2] = "3rd - 1324"
        experiment.PCodes [3] = "noPattern"
        experiment.calculate_stim_properties()

        self.assertEqual(len(experiment.stim_sessionN), experiment.settings.get_maxtrial())
        self.assertEqual(len(experiment.end_at), experiment.settings.get_maxtrial())
        self.assertEqual(len(experiment.stimepoch), experiment.settings.get_maxtrial())
        self.assertEqual(len(experiment.stimblock), experiment.settings.get_maxtrial())
        self.assertEqual(len(experiment.stimtrial), experiment.settings.get_maxtrial())
        self.assertEqual(len(experiment.stimlist), experiment.settings.get_maxtrial())
        self.assertEqual(len(experiment.stim_colorN), experiment.settings.get_maxtrial())
        self.assertEqual(len(experiment.stimpr), experiment.settings.get_maxtrial())

        first_session_last_trial = experiment.settings.epochs[0] * experiment.settings.block_in_epochN * (experiment.settings.blockprepN + experiment.settings.blocklengthN)
        second_session_last_trial = first_session_last_trial + experiment.settings.epochs[1] * experiment.settings.block_in_epochN * (experiment.settings.blockprepN + experiment.settings.blocklengthN)
        third_session_last_trial = second_session_last_trial + experiment.settings.epochs[2] * experiment.settings.block_in_epochN * (experiment.settings.blockprepN + experiment.settings.blocklengthN)

        for i in range(len(experiment.stim_sessionN)):
            if i < first_session_last_trial:
                self.assertEqual(experiment.stim_sessionN[i+1], 1)
            elif i < second_session_last_trial:
                self.assertEqual(experiment.stim_sessionN[i+1], 2)
            else:
                self.assertEqual(experiment.stim_sessionN[i+1], 3)

        for i in range(len(experiment.end_at)):
            if i < first_session_last_trial:
                self.assertEqual(experiment.end_at[i+1], first_session_last_trial + 1)
            elif i < second_session_last_trial:
                self.assertEqual(experiment.end_at[i+1], second_session_last_trial + 1)
            else:
                self.assertEqual(experiment.end_at[i+1], third_session_last_trial + 1)

        for i in range(len(experiment.stimepoch)):
            self.assertEqual(experiment.stimepoch[i+1], i // ((experiment.settings.blockprepN+experiment.settings.blocklengthN)*experiment.settings.block_in_epochN) + 1)

        for i in range(len(experiment.stimblock)):
            self.assertEqual(experiment.stimblock[i+1], i // (experiment.settings.blockprepN+experiment.settings.blocklengthN) + 1)

        for i in range(len(experiment.stimtrial)):
            self.assertEqual(experiment.stimtrial[i+1], i % (experiment.settings.blockprepN+experiment.settings.blocklengthN) + 1)

        count_1 = 0
        count_2 = 0
        count_3 = 0
        count_4 = 0
        sequence = ""
        for i in range(len(experiment.stimlist)):
            if i >= second_session_last_trial: # last session is random
                break;

            trial_num_in_block = i % (experiment.settings.blockprepN+experiment.settings.blocklengthN) + 1
            if trial_num_in_block == 1:
                sequence = ""

            if trial_num_in_block > experiment.settings.blockprepN and (trial_num_in_block - experiment.settings.blockprepN) % 2 == 1:
                if experiment.stimlist[i+1] == 1:
                    count_1 += 1
                    sequence += "1"
                elif experiment.stimlist[i+1] == 2:
                    count_2 += 1
                    sequence += "2"
                elif experiment.stimlist[i+1] == 3:
                    count_3 += 1
                    sequence += "3"
                elif experiment.stimlist[i+1] == 4:
                    count_4 += 1
                    sequence += "4"
                sequence = sequence[-4:]

            if len(sequence) == 4:
                if i < first_session_last_trial:
                    self.assertTrue(sequence == "1243" or sequence == "2431"or sequence == "4312"or sequence == "3124")
                elif i < second_session_last_trial:
                    self.assertTrue(sequence == "1324" or sequence == "3241" or sequence == "2413"or sequence == "4132")

        self.assertEqual(count_1, count_2)
        self.assertEqual(count_2, count_3)
        self.assertEqual(count_3, count_4)

        for i in range(len(experiment.stim_colorN)):
            trial_num_in_block = i % (experiment.settings.blockprepN+experiment.settings.blocklengthN) + 1
            if i < first_session_last_trial: # explicit
                if trial_num_in_block > experiment.settings.blockprepN and (trial_num_in_block - experiment.settings.blockprepN) % 2 == 1:
                    self.assertEqual(experiment.stim_colorN[i+1], "Green")
                else:
                    self.assertEqual(experiment.stim_colorN[i+1], "Orange")
            else: # imlicit or noASRT
                self.assertEqual(experiment.stim_colorN[i+1], "Orange")

        for i in range(len(experiment.stimpr)):
            if i < second_session_last_trial: # explicit or implicit
                trial_num_in_block = i % (experiment.settings.blockprepN+experiment.settings.blocklengthN) + 1
                if trial_num_in_block > experiment.settings.blockprepN and (trial_num_in_block - experiment.settings.blockprepN) % 2 == 1:
                    self.assertEqual(experiment.stimpr[i+1], "P")
                else:
                    self.assertEqual(experiment.stimpr[i+1], "R")
            else: # noASRT
                self.assertEqual(experiment.stimpr[i+1], "R")

if __name__ == "__main__":
    unittest.main() # run all tests