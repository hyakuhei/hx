# Kali-on-k8s - using Kubernetes to parallelize Bug Hunting

The goal here is _not_ to write new software or automation, it’s to use what’s already existing, and figure out how to shove it all onto of K8s to make it:
1. Faster
2. Easier
3. Lower end-node-footprint (should be runnable from a shitty chromebook)

## Setup - one-time operations
1. Get a Kubernetes Cluster ```eksctl create cluster rhodri```
2. Get an EC2 volume to use as a shared volume ```aws ec2 create-volume --availability-zone=us-west-2a --size 10 --volume-type=gp2``` make a note of the VolumeId, you'll need that later.
3. Build a docker-image of Kail with the extra stuff you want, tagged your way (See Dockerfile) ```docker build -t hyakuhei/kali-plus .```
4. Push docker-image to repository of choice (ECR or Dockerhub)

## Disclaimer
Use of these systems, ideas, techniques must be in line with the law. Refer to https://www.hackerone.com/policies/code-of-conduct as a good baseline. Don't do illegal stuff, don't be stupid, stupid!

## DNS Recon 
Most bug bounties come with lists of domains that are in scope. Normally, any subdomain of that domain is in scope, so the first step of recon is to do a bunch of enumeration and brute-forcing of potential domains, to identify what elses might exist.

1. Update domains.txt to include any subdomains you want to inspect/examine
2. 


### Notes on current setup:
EC2 Volume:
```json
{
    "AvailabilityZone": "us-west-2a",
    "CreateTime": "2021-10-17T16:25:49+00:00",
    "Encrypted": false,
    "Size": 10,
    "SnapshotId": "",
    "State": "creating",
    "VolumeId": "vol-09ae9ec414652700c",
    "Iops": 100,
    "Tags": [],
    "VolumeType": "gp2",
    "MultiAttachEnabled": false
}
```